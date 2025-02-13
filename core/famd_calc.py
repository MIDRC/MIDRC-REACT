import prince
import numpy as np
import pandas as pd
import tabulate
import warnings

from core.numeric_distances import scale_feature, calc_distances_via_df


def preprocess_data_for_famd(raw_df, features, numeric_features, scaling_method='standard'):
    """
    Preprocesses the raw data for Factor Analysis of Mixed Data (FAMD).

    Parameters:
    raw_df (DataFrame): The raw data to be preprocessed.
    features (List): List of features to be included in the preprocessing.

    Returns:
    c_data (DataFrame): Preprocessed data with selected features.
    df (DataFrame): Concatenated DataFrame with preprocessed data and 'dataset' column.
    """
    c_data = raw_df.loc[:, features]
    c_data = c_data.dropna(axis=0, how='any') # I don't think this is necessary
    for numeric_feature in numeric_features:
        c_data[numeric_feature] = c_data[numeric_feature].astype(float)
        c_data = scale_feature(c_data, numeric_feature, method=scaling_method)

    return c_data


def fit_famd(data):
    """
    Fits a Factor Analysis of Mixed Data (FAMD) model to the input data.

    Parameters:
    data (pandas.DataFrame): The input data to fit the FAMD model.

    Returns:
    tuple: A tuple containing the fitted FAMD model and the row coordinates.

    Example:
    famd_model, coordinates = fit_famd(data)
    """
    famd = prince.FAMD()
    # Ignore pandas PerformanceWarning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", pd.errors.PerformanceWarning)

        famd = famd.fit(data)
        coordinates = famd.row_coordinates(data)

    return famd, coordinates

def adjust_bin_widths(bins, hist, multiple=2):
    """
    Adjust the width of bins by merging a specified number of adjacent bins.

    Parameters:
    bins (array): The original bin edges.
    hist (array): The original histogram values.
    multiple (int): The factor by which to adjust the bin widths (e.g., 2 to double, 3 to triple).

    Returns:
    new_bins (array): The new bin edges with adjusted widths.
    new_hist (array): The new histogram values corresponding to the new bins.
    """
    # Ensure the bins and histogram values are adjusted by the specified multiple
    new_bins = bins[::multiple]  # Take every 'multiple' bin edge to adjust the bin width
    new_hist = [
        sum(hist[i:i + multiple]) if i + multiple <= len(hist) else sum(hist[i:])
        for i in range(0, len(hist), multiple)
    ]

    return np.array(new_bins), np.array(new_hist)

def calc_famd_df(raw_df, cols_to_use, numeric_cols, dataset_column='_dataset_', bin_width=0.01, print_outliers=False, famd_column='famd_x_coordinates'):
    """
    Calculate the FAMD coordinates for the input DataFrame and return a new DataFrame with the coordinates added.
    Args:
        raw_df:
        cols_to_use:
        numeric_cols:
        dataset_column:
        bin_width:
        print_outliers:
        famd_column:

    Returns:

    """
    c_df = preprocess_data_for_famd(raw_df, cols_to_use, numeric_cols)
    _, coordinates = fit_famd(c_df)
    x_coordinates = coordinates[0]

    # Add dataset column to the DataFrame after FAMD fitting
    c_df[dataset_column] = raw_df[dataset_column].astype(str)
    column_series = pd.Series(x_coordinates)
    # Put the x coordinates in a new column
    c_df = c_df.assign(**{famd_column: column_series})

    # Print outliers
    if print_outliers:
        outlier_cutoff = 3.5
        outlier_df = c_df[c_df[famd_column].abs() > outlier_cutoff]
        if len(outlier_df) > 0:
            outlier_df = outlier_df.sort_values(by=famd_column, ascending=False)
            print(f"Outliers in FAMD fitting: {outlier_df.shape[0]}")
            print(tabulate(outlier_df, headers='keys', tablefmt='psql'))

    return c_df

def calc_famd_distances(df, cols_to_use, numeric_cols, dataset_column='_dataset_', distance_metrics=('all'), jsd_scaled_bin_width=0.01, print_outliers=False):
    """
    Calculate various distance metrics based on FAMD coordinates calculated from the input DataFrame using the feature
    columns specified in the SamplingData object.

    This function computes Jensen-Shannon Divergence (JSD),
    Wasserstein distance, Kolmogorov-Smirnov (KS) statistics,
    and Cucconi distance, with optional scaling methods for
    the given distances. The results are returned as a
    dictionary where keys represent the metric names.

    Parameters:
    - df (DataFrame): The DataFrame containing the data.
    - sampling_data (SamplingData): Object containing dataset information.
    - distance_metrics (tuple): A tuple of strings specifying which distance metrics to compute.
                               Use 'all' to compute all available metrics or specify individual metrics
                               (e.g., 'jsd', 'wass', 'ks2', 'cuc') along with optional scaling
                               options (e.g., 'wass(std)', 'ks2(rob)', etc.).
    - jsd_scaled_bin_width (float): Width of each histogram bin for scaled JSD (default is 0.01).
    - print_outliers (bool): Whether to print outliers (default is False).

    Returns:
    - dict: Dictionary of distance values specified in distance_metrics for each dataset combination.
    """
    return calc_distances_via_df(calc_famd_df(df, cols_to_use, numeric_cols, print_outliers=print_outliers),
                                 'famd_x_coordinates',
                                 dataset_column,
                                 distance_metrics=distance_metrics,
                                 jsd_scaled_bin_width=jsd_scaled_bin_width,
                                 )

def calc_famd_ks2_at_date(df1, df2, cols_to_use, numeric_cols, calc_date):
    df1_at_date = df1[df1['date'] <= calc_date]
    df2_at_date = df2[df2['date'] <= calc_date]
    df_list = [df1_at_date, df2_at_date]

    dataset_column = '_dataset_'
    labels = [f'Dataset {i}' for i in range(len(df_list))]  # Dataset labels
    combined_df = pd.concat(
        [df.assign(**{dataset_column: label}) for label, df in zip(labels, df_list)],
        ignore_index=True
    )

    distance_metrics = ['ks2']
    distance_dict = calc_famd_distances(combined_df, cols_to_use, numeric_cols, dataset_column, distance_metrics=distance_metrics)
    print('KS2 distance at date:', calc_date)
    print(distance_dict['ks2'])
    return distance_dict['ks2']['Dataset 0 vs Dataset 1']


def calc_famd_ks2_at_dates(df1, df2, cols_to_use, numeric_cols, calc_date_list):
    df_list = [df1, df2]

    dataset_column = '_dataset_'
    labels = [f'Dataset {i}' for i in range(len(df_list))]  # Dataset labels
    combined_df = pd.concat(
        [df.assign(**{dataset_column: label}) for label, df in zip(labels, df_list)],
        ignore_index=True
    )

    famd_df = calc_famd_df(combined_df, cols_to_use, numeric_cols)

    # Add date column to the DataFrame after FAMD fitting
    famd_df['date'] = combined_df['date']

    ks2_values = []
    for calc_date in calc_date_list:
        distance_metrics = ['ks2']
        distance_dict = calc_distances_via_df(famd_df[famd_df['date'] <= calc_date],
                                              'famd_x_coordinates',
                                              dataset_column,
                                              distance_metrics=distance_metrics)
        ks2_values.append(distance_dict['ks2']['Dataset 0 vs Dataset 1'])

    return ks2_values
