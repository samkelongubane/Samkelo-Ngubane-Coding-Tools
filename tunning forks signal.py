#plotting curves for voltage capacitor and voltage source 
#importing the necessary modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#importing data into the python environment

f = open('peak magnitude pre-filtured.txt','r')
header = f.readline()

i = 0
time = np.zeros(1000)
volt = np.zeros(1000)


for line in f:
    line = line.strip()
    columns = line.split()
    time[i] =float(columns[0])
    volt[i] = float(columns[1])
    #print(frequency[i], volt[i])
    i = i + 1

#plotting the voltage curve
plt.plot(time, volt)
plt.title('Peak Magnitude Pre Filture')
plt.ylim(0.00, 0.00000007)
plt.xlim(0.00, 5000)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Peak Magnitude [V]')
plt.show()
