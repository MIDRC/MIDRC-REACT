#  Copyright (c) 2025 Medical Imaging and Data Resource Center (MIDRC).
#
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

"""
This module contains functions for processing TSV files downloaded from the data.MIDRC.org website.
"""

from datetime import datetime
import re

import pandas as pd

def process_dataframe(df):
    """Applies both transformations on a pandas DataFrame."""
    df['date'] = pd.to_datetime(datetime.today().date())
    return df

def preprocess_data(df):
    """Preprocesses a pandas DataFrame."""
    return process_dataframe(df)

