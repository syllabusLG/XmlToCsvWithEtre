#install pandas with pip install pandas

import pandas as pd

#Read the plat file as csv and create dataframe
dataframe1  = pd.read_csv("employees.txt")

#Convert the dataframe as csv file
dataframe1.to_csv("employees.csv", index= None)