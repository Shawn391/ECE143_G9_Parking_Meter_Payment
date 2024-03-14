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

### Data sources:
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
