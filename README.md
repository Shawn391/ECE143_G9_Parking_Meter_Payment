<!------------------------------------------ TITLE BLOCK --------------------------------------------------------------->
<h1 align="center"> Group 9: Analysis and Visualization of San Diego Parking Transactions </h1>

<p align="center">
    Course Project for UCSD ECE 143: Programming for Data Analytics
    <br /> <br />
    <a href="https://github.com/anshuldevnani"> Anshul Devnani </a>
    ·
    <a href="https://github.com/kdivij"> Divij Divij </a>
    ·
    <a href="https://github.com/Shawn391"> Xiang Gao </a>
    ·
    <a href="https://github.com/nolanlyc"> Yuchuan Li </a>
    ·
    <a href="https://github.com/GreatSnoopyMe"> Tianyue Li </a>
</p>


<!------------------------------------------ TABLE OF CONTENTS ---------------------------------------------------------->
<details open="open">
  <summary><h2 style="display: inline-block"> Table of Contents </h2></summary>
  <ol>
    <li>
      <a href="#about-the-project"> About The Project </a>
      <ul>
        <li><a href="#key-questions"> Key Questions </a></li>
        <li><a href="#data-sources"> Data Sources </a></li>
        <li><a href="#job-to-be-done"> Job To Be Done </a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started"> Getting Started </a>
      <ul>
        <li><a href="#prerequisites"> Prerequisites </a></li>
        <li><a href="#how-to-run"> How To Run </a></li>
      </ul>
    </li>
    <li><a href="#file-architecture"> File Architecture </a></li>
  </ol>
</details>

<!------------------------------------------ About The Project ---------------------------------------------------------->
## About The Project
In the bustling urban landscape of San Diego, optimizing urban mobility and enhancing the parking experience stand as pivotal challenges that impact both residents and visitors alike. The essence of these challenges lies in the efficient utilization of parking spaces, a task that is instrumental in reducing congestion, improving accessibility, and maximizing the revenue generated from parking resources.

Our project, driven by the City of San Diego's Open Data Portal, leverages detailed datasets on parking meter transactions and locations to embark on a comprehensive analysis and refinement of parking management strategies. These datasets, detailing meter placements, zones, transaction records since 2018, and more, offer a rich foundation for our analytical endeavors. Through this analysis, we aim to unravel patterns in parking usage, identify peak times and areas of high demand, and predict revenue generation across different parking zones. Such insights are not only crucial for improving the usability of parking spaces but also contribute significantly to the overall efficiency of urban transportation systems.

The necessity for this project arises from the growing complexities of city life, where the harmonious flow of traffic and the availability of parking spaces become essential for the daily routines of countless individuals. By employing data analysis techniques and visualization tools, our project seeks to address several following key questions.

With a proposed solution that encompasses data analysis, visualization, we expect to get results that not only aids in strategic budgeting and resource allocation but also enhances the parking experience for everyone involved. The real-world application of our project envisions a future where finding a parking spot in San Diego is no longer a hassle but a seamless part of city living, guided by data-driven insights and policies.

This initiative reflects our commitment to improving urban mobility in San Diego, contributing to a more accessible and efficiently managed city. Through our project, we aspire to make a contribution for how data can be utilized to solve real-world transportation challenges, making San Diego a better city to live and study.

### Key Questions 
* When are the peak hours for parking meter transactions in San Diego, and how do they vary across different areas?
* Which areas experience consistently high or low parking space occupancy?
* Can we predict revenue generation for different parking zones based on historical transaction data and location information?
* What is the approximate probability of finding available parking spaces at a certain location during a specific time period?

### Data sources
Visualization of San Diego Parking Meter System based on historical location and payment datasets.
Here's an overview of each dataset and the parameters we have chosen to focus on:

**Parking Meters Locations Dataset:** This dataset offers comprehensive information on the placement of parking meters throughout San Diego, detailed in CSV format. It includes data on meter zones, areas, and specific locations identified by pole-ids. This rich dataset allows us to understand the spatial distribution of parking meters and identify zones with varying parking capacities and demands.

**Parking Meters Transactions Dataset:** Recording all meter transactions since 2018 to 2023, this dataset is available in both raw and aggregated forms, making it invaluable for analyzing parking usage patterns and revenue generation. Time-segmented data aids in identifying peak parking hours, assessing the popularity of certain areas, and optimizing parking operations. From this dataset, we analyze parameters including:

* Time information: year, month, day of the week, and approximate time of transactions, helping us understand parking demand across different times and seasons.
* Payment details: including payment methods and transaction amounts, offering insights into revenue streams and user payment preferences.
* Meter expiration and transaction start dates and times, providing data on parking duration and turnover rates.

treas_parking_meters_loc_datasd.csv: 	https://data.sandiego.gov/datasets/parking-meters-locations/

treas_parking_payments_2023_datasd.csv: https://data.sandiego.gov/datasets/parking-meters-transactions/

### Job To Be Done
1. Preprocess Data
* Clean datasets by removing duplicates and irrelevant entries.
* Link related data across datasets, such as matching locations with transactions.
2. Analyze Data
* Examine statistical properties and relationships between parameters like time, payment method, and meter type.
* Identify key patterns such as peak usage times and revenue trends.
3. Visualize Data
* Use charts, graphs, and maps to present insights clearly.
* Highlight parking demand, revenue patterns, and parking availability visually.


<!------------------------------------------ Getting Started ---------------------------------------------------------->
## Getting Started
### Prerequisites
Clone the repository:
```
git clone https://github.com/Shawn391/ECE143_G9_Parking_Meter_Payment
```
#### Third Party Modules
Install the following dependencies:
* csv
* Jupyter
* PyTorch
* notebook
* pandas
* torch  
* numpy   
* random  
* matplotlib.pyplot
* json

or alternatively run,
```
pip install -r requirements.txt
```
### How To Run

1. Data_Preprocessing: pre_process.py and preprocess_func.py
* Download treas_parking_meters_loc_datasd.csv and treas_parking_payments_2023/2022/2021/2020/2019/2018_datasd.csv
* Ensure the script and datasets are the in the same directory or change the file path in the read_csv function
* Ensure all third party modules are installed
* Run
2. data_statistic.py: preprocess_func.py and space_occu_analysis.py
* Download treas_parking_meters_loc_datasd.csv and treas_parking_payments_2023/2022/2021/2020/2019/2018_datasd.csv
* Ensure the script and datasets are the in the same directory or change the file path in the read_csv function
* Ensure all third party modules are installed
* More detailed description step by step can be found in the python file, hope you can find something interesting results in this file.
* Run
3. data_visualization.ipynb:
* Download all raw data files
* Ensure the script and datasets are the in the same directory or change the file path in the read_csv function
* Ensure all third party modules are installed
* More detailed description step by step can be found in the ipynb file, hope you can find something interesting results in this file.
* Run
4. getAllrevenue.py
* Download all raw data files, and store the data under `revenue_analysis/dataset`
* More detailed description step by step can be found in the `.py` file, hope you can find something interesting results in this file.
* Run


<!------------------------------------------ File Architecture  ---------------------------------------------------------->
## File Architecture
```
[ECE143_G9_Parking_Meter_Payment]
├─ 📁revenue_analysis
    ├─ 📄allYear.json
    ├─ 📄getAllrevenue.py
├─ 📁time_analysis_eric
    ├─ 📄parking_percentage_by_hours_per_area.csv
    ├─ 📄parking_time_by_area_weekday.csv
    ├─ 📄parking_time_by_area_weekend.csv
    ├─ 📄parking_time_by_hours_per_area.csv
    ├─ 📄parking_time_by_area_whole_week_2020.csv
    ├─ 📄parking_time_by_area_whole_week_2021.csv
    ├─ 📄parking_time_by_area_whole_week_2022.csv
    ├─ 📄parking_time_by_area_whole_week_2023.csv
    ├─ 📄parking_time_by_hours_per_area.csv
    ├─ 📄pre_process.py
    ├─ 📄preprocess_func.py
    ├─ 📄space_occu_analysis.py
├─ 📁Jupyter_notebook
    ├─ 📄space_occu_analysis.ipynb
    ├─ 📄map_visualization.ipynb
    ├─ 📄rev_analysis.ipynb
    ├─ 📄parking_probability-final.ipynb
├─ 📄LICENSE
├─ 📄requirements.txt
├─ 📄README.md
```
