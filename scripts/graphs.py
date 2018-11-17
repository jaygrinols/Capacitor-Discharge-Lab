from sys import argv 
import re 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

script, csv_name = argv 
data = pd.read_csv(csv_name)

T = data['Time_(s)'].values
V = data['Potential_(V)'].values
ln_V = np.log(V)
graph_title = os.path.basename(csv_name)[0:-4]

#Use subplots?

plt.subplot(211)
plt.plot(T, V, color='green')
plt.grid(True)
plt.title(graph_title)
plt.ylabel('Electric Potential (V)')


plt.subplot(212)
plt.plot(T, ln_V, color='purple')
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('ln(V)')
plt.savefig('./figures/' + os.path.basename(csv_name[0:-4]) + '.png')