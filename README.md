# Physics-Capacitor-Discharge-Lab

Measuring theoretical vs. experimental values of 
CSV formatting requirements: 
-Name: '[resistance value]-ohms.csv'
-Attributes: Time_(s), Potential_(V)

How to use: 
python [script path] [csv path]

Descriptions: 
graphs.py: 
Given a csv dataset of Electric Potential vs. Time, generates graphs of V vs. T and ln(V) vs. T. Saved to 'figures' directory.
data_analysis.py: 
Using a linear regression, calculates the slope for ln(V) vs. T and compares it to the theoretical value of -1/(RC), saves percent error to 'results.txt'.
See 'Capacitor_Discharge.pdf' for the derivation. 
dataset of Electric Potential vs. Time

