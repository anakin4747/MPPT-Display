""" 
Things to do:
    - Open data from a CSV File to plot a curve
"""

import matplotlib.pyplot as plt # for plotting
from matplotlib.animation import FuncAnimation # for live data
from connect2Device import connect2USB # for reading USB data
from measure import getMeasurements # for extracting data from USB
import keyboard # for ctrl-c quitting functionality
import csv # for logging and loading data
import datetime # for dating files


SIZE = 10 # Practically a define but its not C so its a variable

plt.style.use('fivethirtyeight') # Plot style

############################################################
import numpy as np # for graphing functions
# Possibly delete if you stop using linspace()

VLine = np.linspace(0, 6, 14)
ILine = np.linspace(0, 6, 14)
PLine = np.linspace(30, 0, 14)
# This will get replaced by measured values
############################################################

fig, ax1 = plt.subplots() # Create plot object
ax2 = ax1.twinx() # Create a second y axis

Vdata = []
Pdata = []
reading = ""
# Declaring arrays that will grow

ser = connect2USB()
# Connect to USB with error handling

def checkIfCtrlC(): # Ctrl-c quitting functionality
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
        ser.close() # Close serial connection
        exit() # Kill program


date = datetime.datetime.now().strftime("%B-%d-%H-%M-%S")

with open('logs/VIVPcurves.csv', 'r') as curvesFile, \
    open(f'logs/measured-data-{date}.csv', 'w', newline='') as dataFile:
    # Opening files for curves to plot and data to log

    writer = csv.writer(dataFile)
    reader = csv.reader(curvesFile)
    # Open csv I/O objects

    writer.writerow(["CH0", "CH1", "CH2"])
    # Label columns
    

    def animate(i):
    
        measurements = getMeasurements(reading, ser)

        if 1000 not in measurements:
            writer.writerow(measurements)

        print("Ch0 - Input Voltage = {:6.3f} Volts\t".format(measurements[0]) + \
            "Ch1 - Input Current = {:6.3f} Amps\t".format(measurements[1]) + \
            "Ch2 - Battery Voltage = {:6.3f} Volts".format(measurements[2]))
    
        ax1.cla()
        ax2.cla()
        # Clear each axes
    
        ax1.plot(VLine, ILine, linestyle='--', linewidth=1.5)
        # Setting line weight and style
        ax1.set_xlabel('Voltage (V)')
        ax1.set_ylabel('Current (A)')
        # Setting axis labels
    
        ax2.plot(VLine, PLine, linestyle='--', linewidth=1.5)
        # Setting line weight and style
        ax2.set_ylabel('Power (W)', labelpad=15)
        # Label kept over lapping the ax1.ylabel - this fixed it
        ax2.yaxis.set_label_coords(1.075, 0.5)
    
        Vdata.append(measurements[0])
        Pdata.append(measurements[0] * measurements[1])
        # Update data points
    
        ax2.scatter(Vdata[-SIZE:-1], Pdata[-SIZE:-1], \
                marker='o', color='red')
        # Real-time data except the most recent data point
    
        ax2.scatter(Vdata[-1], Pdata[-1], marker='o', color='blue')
        # Real-time most recent data point
    
        checkIfCtrlC()
    
    
    ani = FuncAnimation(plt.gcf(), animate, interval=100, \
            cache_frame_data=False)
    # Run animate function every 100ms, don't cache data to suppress error
    
    plt.tight_layout() # Formatting
    plt.show() # Plot plt
    
