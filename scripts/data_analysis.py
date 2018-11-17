from sys import argv 
import numpy as np 
import pandas as pd 

script, csv_name = argv 
data = pd.read_csv("../csv_data/" + csv_name)

T = data['Time_(s)'].values
V = data['Potential_(V)'].values
ln_V = np.log(V)

