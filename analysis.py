from sys import argv 
import re 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

script, csv_name = argv 
data = pd.read_csv(csv_name)


T = data['Time_(s)'].values
V = data['Potential_(V)'].values
ln_V = np.log(V)
graph_title = ' '.join(re.split('[-.]', csv_name)[:-1]) + ' resistor'

#Use subplots?
#test

plt.plot(T, V, color='green')
plt.grid(True)
plt.title(graph_title)
plt.xlabel('Time (s)')
plt.ylabel('Electric Potential (V)')
plt.show()

plt.plot(T, ln_V, color='orange')
plt.title(graph_title)
plt.xlabel('Time (s)')
plt.ylabel('ln(V)')
plt.show()