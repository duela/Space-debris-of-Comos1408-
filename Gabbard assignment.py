# -*- coding: utf-8 -*-
"""
Created on Sun May 15 02:03:18 2022

@author: yinku
"""
import math

import pylab as plt
from matplotlib.transforms import Bbox

TLE_file = "Cosmos1408.txt"
with open(TLE_file, 'r') as f:    # Opening Txt file
  TLE_data = f.read()              # Reading Txt file
    
TLE_data = TLE_data.split("\n")    # Spliting Txt file 

gravity = 3.986004e14
y = math.pi 

X_ = []                            # Empty arrays 
Y_ = []
Z_ = []
for i in range(0, len(TLE_data), 3):     # Txt file has a 318 lines 
  nam = TLE_data[i]
  name = nam.rstrip()
  dte = TLE_data[i+2]                    # Read only the 3rd lines 
  line = dte.rstrip()                    # to eliminate the unwanted blanks and turn the line into a list of words
  line = dte.split()
  mean_motion = line[7]                  # extract data of the 8 list in every 3rd line
  n = str((mean_motion))                 # convert to string
  mn = float(n)                          # convert to float
  eccentricity = line[4]                 # extract data of the 5 list in every 3rd line
  ecc = str(eccentricity)                # convert to string
                           # convert to string bacck
  ent = '0.'+ecc                          # add 0. to the begin of the value
  e = float(ent)                         # convert to float
  major = (gravity**(1/3))/(((2*y*(mn))/(86400))**(2/3))       # semi-major axis calculation
  period = ((2*y)*(((major**3)/gravity)**0.5)/60)              # period calculation convert for seconds to mins
  Rp = (major*(1-e))/1000                            #Apogee convert to Km
  Ra = (major*(1+e))/1000                             #Perigeeconvert to Km
 
  print('Perigee: ', Rp, 'Km')
  print('Apogee: ', Ra, 'Km')
  print('Period: ', period, 'mins')
  X_.append(period)                        # Store values into an array
  Y_.append(Rp)
  Z_.append(Ra)

# To Plot Gabbard diagram 
plt.plot(X_,Z_,  linewidth = 0.8, linestyle = 'dotted',label = 'Apogee')
plt.plot(X_,Y_, linewidth = 0.8, linestyle = 'dotted',label = 'Perigee')
plt.title('Gabbard diagram Plot')
plt.legend(loc='best')
plt.xlabel('eriod (mins)', fontsize=9)
plt.ylabel(' Altitude, (Km)', fontsize=9)
plt.grid()
plt.show()


