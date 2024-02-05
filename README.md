# Homework-2.0

### This files contains the scripts and logic for data loading, transforming and data exporting.

#### Question 1. Data Loading
Once the dataset is loaded, what's the shape of the data?

266855 rows x 20 columns                 15.528s


#### Question 2. Data Transformation
Upon filtering the dataset where the passenger count is greater than 0 and the trip distance is greater than zero, how many rows are left?

139370 rows x 21 columns                 3.615s


#### Question 3. Data Transformation
Which of the following creates a new column lpep_pickup_date by converting lpep_pickup_datetime to a date?

data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date


#### Question 4. Data Transformation
What are the existing values of VendorID in the dataset?

Rows with zero passengers: 661

Rows with zero trip_distance: 7362

 

0         2

1         2

2         2

3         1

4         1

         ..

230012    2

230013    2

230014    2

230015    2

230016    2

Name: vendorid, Length: 139370, dtype: Int64


#### Question 5. Data Transformation
How many columns need to be renamed to snake case?

4


#### Question 6. Data Exporting
Once exported, how many partitions (folders) are present in Google Cloud?

