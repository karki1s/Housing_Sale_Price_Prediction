# Housing_Sale_Price_Prediction

I did this project while taking Data Engineering class at Central Michigan University. For this project I collected data from zillow.com website. Using python programming language and library like sklearn, numpy, and matplotlib; I analyzed data to come off with the linear regression model which best represent the sale price for the house using the attributes like age, bed rooms, house size, and lot size. 
Once I have a raw data collected form zillow.com, I use the DataFiltter.py script to clean the data, and change to appropriate format. Data mutation was done using appropriate measures by analyzing several plot (using Exploratory Data Analysis).  Once we run DataFiltter.py script we get clean dataset which is saved in the file called reg.txt.
Clean dataset is divided into training and test dataset using the TrainingTestSplit.py script. Here we decided 80% training and 20% for test but can be changed easily. Training dataset is used for creating the linear regression model and test dataset is used to evaluate and compare our result with actual sold price and Zillow’s estimate price(zestimate). 
Our model and the prediction is generated using CreateModel.py script which will generate some plots and result_out file which will have the prediction and model equation. 

Here I included the raw_data.csv, DataFilter.py, CheckNoise.py, TrainTestSplit.py, CreateModel.py.

# How to use these Script:

First run DataFilter.py which will read raw_dat.csv and make the data appropriate for analyzing and saves it to reg.txt. It will create several plots for Exploratory Data Analysis. 

Second run the CheckNoise.py script which reads the reg.txt data file and generates various plot for Exploratory Data Analysis. 

Third run the TrainingTestSplit.py which uses the reg.txt datafile and generate the training dataset called (trainlst.txt) and test dataset called test.txt.

Finally, run the CreateModel.py script which will use the trainlst.txt dataset and create the approprate model. It also generate the prediction for the test dataset (test.txt) and save to the result_out. In the result_out file you can find Zestmate, Sold Price, Predicted Value as well as last row in the file will have model (equaltion) to predict the price of a house by giving approprate attributes. 



