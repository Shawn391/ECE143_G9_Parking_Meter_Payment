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
* When are the peak hours and days for parking meter transactions in San Diego, and how do they vary across different areas?
* Which areas experience consistently high or low parking space occupancy, and are there geographical patterns in parking demand?
* Which areas experience consistently high or low parking space occupancy, and are there geographical patterns in parking demand?
* How does parking demand change between weekday and weekend, and are there opportunities for seasonal adjustments in parking management policies?
* What is the approximate probability of finding available parking spaces at a certain location during a specific time period?
### Data sources
Visualization of San Diego Parking Meter System based on historical location and payment datasets

treas_parking_meters_loc_datasd.csv: 	https://data.sandiego.gov/datasets/parking-meters-locations/

treas_parking_payments_2023_datasd.csv: https://data.sandiego.gov/datasets/parking-meters-transactions/
### Job To Be Done



<!------------------------------------------ Getting Started ---------------------------------------------------------->
## Getting Started
### Prerequisites
Clone the repository:
```
git clone https://github.com/Shawn391/parking-meter-payment
```
#### Third Party Modules
Install the following dependencies:
* csv  
* Ridge  
* numpy   
* random  
* matplotlib.pyplot 

or alternatively run,
```
pip install -r requirements.txt
```
### How To Run

data_preprocessing.py:
1. Download ....csv and ....csv
2. Ensure the script and datasets are the in the same directory
3. Ensure all third party modules are installed
4. Run

data_visualization.ipynb:
1. Download all raw data files
2. Ensure the script and datasets are the in the same directory or change the file path in the read_csv function
3. Ensure all third party modules are installed
4. More detailed description step by step can be found in the ipynb file, hope you can find something interesting results in this file.
5. Run

data_statistic.py:
1. Download treas_parking_meters_loc_datasd.csv and treas_parking_payments_2023_datasd.csv
2. Ensure the script and datasets are the in the same directory or change the file path in the read_csv function
3. Ensure all third party modules are installed
4. More detailed description step by step can be found in the python file, hope you can find something interesting results in this file.
5. Run

<!------------------------------------------ File Architecture  ---------------------------------------------------------->
## File Architecture
ECE 143 Group 9 Project.pdf: Final presentation slides

data_visualization.ipynb: Visualization of ...

treas_parking_meters_loc_datasd.csv: original dataset including ....  

treas_parking_payments_2023_datasd.csv: original dataset including ....  

...: processed dataset of....
