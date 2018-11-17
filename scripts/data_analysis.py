from sys import argv 
import numpy as np 
import pandas as pd 
import re 

script, csv_name = argv 
data = pd.read_csv(csv_name)
results = open('results.txt', 'w')

T = data['Time_(s)'].values
V = data['Potential_(V)'].values
ln_V = np.log(V)

f = np.polyfit(T, ln_V, 1)
slope, intercept = f 

resistance = int(re.findall(r'\d+', csv_name)[-1])
capacitance = 1 
theoretical_slope = -1/resistance/capacitance
percent_error = (slope - theoretical_slope)/theoretical_slope * 100
results.write("""++++++++++++++++++++++++++++++++++
Resistance: {} Ohms
Experimental -1/Tau: {} 
Calculated -1/Tau: {}
Percent Error: {}%
""".format(resistance, slope, theoretical_slope, percent_error))




