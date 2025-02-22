                  
 
<h1 align="center" style="font-weight: bold;">MIDRC-REACT Representativeness Exploration and Comparison Tool</h1>

<p align="center">
<a href="#tech">Technologies</a> |
<a href="#started">Getting Started</a> |
<a href="#colab">Collaborators</a> |
<a href="#references">References</a> |
<a href="#contribute">Contribute</a>
</p>

<p align="center">
<a href="https://www.midrc.org/">📱 Visit MIDRC Website</a>
</p>

<h2>:information_source: Overview</h2>

The MIDRC Representativeness Exploration and Comparison Tool (REACT) is a tool designed to compare the representativeness of biomedical data. 
By leveraging the Jensen-Shannon distance (JSD) measure, this tool provides insights into the demographic representativeness of datasets within the biomedical field.
It also supports monitoring the representativeness of datasets over time by assessing the representativeness of historical data.
Developed and utilized by MIDRC, this tool assesses the representativeness of data within the open data commons to the US population.
Additionally, it can be generalized by users for other dataset representativeness needs, such as assessing the similarity of demographic distributions across multiple attributes in different biomedical datasets.

<h2>:wrench: Features</h2>

* **Jensen-Shannon Distance (JSD) Calculation**: Uses the JSD measure to assess the representativeness of data.
* **Comparative Analysis**: Enables comparisons between different datasets to evaluate population representativeness.
* **Biomedical Focus**: Specifically tailored for analyzing biomedical data, ensuring relevance and similarity.
* **Historical Data**: Enables the ability to assess data over time for monitoring changes in representativeness.

<h2>:notebook_with_decorative_cover: Background</h2>

The methodology behind MIDRC-REACT is based on the 2023 paper by Whitney et al. titled 
<a href="#1">"Longitudinal assessment of demographic representativeness in the Medical Imaging and Data Resource Center open data commons"[1]</a>. 
This paper provides the theoretical foundation for using JSD in evaluating demographic representativeness.

![screenshot](docs/images/screenshot.jpg)

<h2 id="technologies">💻 Technologies</h2>

Technologies used with this application
* Python
* PySide6
* numpy
* scipy
* pandas

There is a requirements.txt file available to install requirements

<h2 id="started">🚀 Getting started</h2>

#### Configure yaml
First, configure your own jsdconfig.yaml file to select which data to load by default. There is a jsdconfig-example.yaml file provided that may be copied over or used as a template for your own config file.
* The filename needs to be specified, and a human-readable name should be provided for use in the plots and figures. 
* Please see the ***Generating custom Excel files*** section for additional information.
* On your first run, you may use ```cp jsdconfig-example.yaml jsdconfig.yaml``` to load the MIDRC data.

#### Run application
To start the application, run `python main.py`

#### Generating plots and figures
* Select the files you wish to compare in the drop-down menus that you wish to make comparisons between. 
* A checkbox is provided next to the drop-down menus to select whether additional plots should be shown for each individual file selected. 
* Note: displaying plots for two or more files simultaneously may require a 4k monitor

#### Generating custom excel files
- Use the provided MIDRC, CDC, and Census Excel files as an example on how to prepare your custom data. 
- For each date, ***cumulative sums are expected***.
- **Each attribute should have its own sheet** which will be automatically parsed by the application.
- Column names within each sheet are parsed and compared between files
  - Where there is a matching column name within a worksheet of the same name, the JSD will be calculated using those values.
  - ***A Date column is expected***, and it should be sorted. Please see how the census data is loaded using the example config file if your data does not have multiple dates, and you do not have a date column.
- The list of attributes provided in the GUI should be a list where worksheets with an identical name exist in both files. If it is not, please check your spelling
- The ```remove column name text``` config parameter is due to how the MIDRC data is generated. There is a ```(CUSUM)``` suffix that needs to be removed to compare it to CDC and Census data.

#### GUI Manipulation
The plots and figures should be movable, adjustable, re-sizable, or hidden. 

To see the list of available dock widgets, you can right-click on any menu/title bar area, i.e. either the main window menu bar or any title bar in a dock widget. This is useful if you hide one of hte docked widgets and wish to view them again.

Keyboard commands may be used to copy and paste the calculated JSD values (and dates) and pasted in Excel or a notebook as tab-delimited data.

 
<h3>Prerequisites</h3>

- Python 3.9 or highter
- [Git](https://github.com)
 
<h3>Cloning</h3>

How to clone the project

```bash
git clone https://github.com/MIDRC/MIDRC_Diversity_Calculator.git
```
 
<h3>Installing Requirements</h3>

You may install project dependencies using pip.

Using pip:

```bash
cd MIDRC_Diversity_Calculator
python -m pip install --upgrade pip
pip install -r requirements.txt
```

<h3>Starting</h3>

How to start the project

```bash
cd MIDRC_Diversity_Calculator
cp jsdconfig-example.yaml jsdconfig.yaml
python main.py
```
 
<h2 id="colab">🤝 Collaborators</h2>

<h3>Special thank you for all people that contributed for this project</h3>
<table>
<tr>

<p>
Robert Tomek,
Maryellen Giger,
Heather Whitney
</p>
<h3>We'd also like to acknowledge</h3>

Natalie Baughan, 
Kyle Myers, 
Karen Drukker, 
Judy Gichoya, 
Brad Bower, 
Weijie Chen, 
Nicholas Gruszauskas, 
Jayashree Kalpathy-Cramer,
Sanmi Koyejo,
Rui Sá,
Berkman Sahiner,
Zi Zhang,

#### The MIDRC Bias and Diversity Working Group:
* Co-leads
  * Karen Drukker
  * Judy Wawira Gichoya
* AAPM
  * Weijie Chen
  * Kyle Myers
  * Heather Whitney
* ACR
  * Jayashree Kalpathy-Cramer
* RSNA
  * Zi Jill Zhang
* NIH
  * Rui Sá
  * Brad Bower
* MIDRC Central (University of Chicago)
  * Maryellen Giger
  * Nick Gruszaukas,
  * Katie Pizer
  * Robert Tomek
* Project Manager
  * Emily Townley

</tr>
</table>

<h2 id="references">:book: References</h2>
<a id="1">[1]</a> 
Whitney HM, Baughan N, Myers KJ, Drukker K, Gichoya J, Bower B, Chen W, Gruszauskas N, Kalpathy-Cramer J, Koyejo S, Sá RC, Sahiner B, Zhang Z, Giger ML. 
Longitudinal assessment of demographic representativeness in the Medical Imaging and Data Resource Center open data commons. 
J Med Imaging (Bellingham). 2023 Nov;10(6):61105. 
<a href="https://doi.org/10.1117/1.JMI.10.6.061105">doi: 10.1117/1.JMI.10.6.061105</a>. Epub 2023 Jul 18. PMID: 37469387; PMCID: PMC10353566.
 
<h2 id="contribute">📫 Contribute</h2>

1. `git clone https://github.com/MIDRC/MIDRC_Diversity_Calculator.git`
2. `git checkout -b feature/NAME`
3. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!
 
<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

 
<h2 id="license">:heavy_check_mark: License</h2>
This project is licensed with the Apache 2.0 license. See LICENSE file for details.


<h2 id="acknowledgement">Acknowledgement</h2>
<em>This work was supported in part by The Medical Imaging and Data Resource Center (MIDRC), which is funded by the National Institute of Biomedical Imaging and Bioengineering (NIBIB) of the National Institutes of Health under contract 75N92020D00021/5N92023F00002 and through the Advanced Research Projects Agency for Health (ARPA-H).</em>
