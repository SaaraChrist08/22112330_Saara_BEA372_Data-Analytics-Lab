## Bank Data Analysis
This repository contains Python code for analyzing a bank dataset stored in a CSV file. The code performs the following tasks:

1. Reads the bank dataset from a CSV file.
2. Displays the headers of the dataset.
3. Counts the number of married, single, and divorced people in the dataset.
4. Prepares a histogram for the age distribution in the dataset.
   
## Dataset
The dataset used for analysis is stored in the file bank.csv, located at D:\CHRIST UNIVERSITY\DALMP\. Make sure to provide the correct file path when executing the code.

## Code Files
DALMP.py: Contains the Python code for analyzing the bank dataset.

## Usage
1. Ensure that you have Python installed on your system.
2. Clone this repository or download the DALMP.py file.
3. Modify the file path in the code to match the location of your bank.csv file.
4. Open a terminal or command prompt and navigate to the directory where the analyze_bank_data.py file is located.

## Functions
# header()
This function displays the headers of the dataset. It reads the first line of the dataset and splits it into individual headers.

# marital(data)
This function counts the number of married, single, and divorced people in the dataset. It iterates through each data entry and extracts the marital status information. The counts are then printed to the console.

# prepare_age_histogram(data)
This function prepares a histogram for the age distribution in the dataset. It extracts the age of each customer from the dataset and groups them into age classes. The histogram is displayed, showing the age range and the number of customers falling within each range.


