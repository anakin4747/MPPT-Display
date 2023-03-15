""" 
Things to do:
    - Save data to a CSV File
    - Open data from a CSV File
"""

import matplotlib.pyplot as plt # for plotting
from matplotlib.animation import FuncAnimation # for live data
import keyboard # for ctrl-c quitting functionality
import serial # for reading USB data
import re # for processing text 
import numpy as np # for graphing functions
import csv # for logging and loading data
import time # for waiting to retry serial read
import datetime # for dating files

import random # Possibly delete in future


SIZE = 10 # Practically a define but its not C so its a variable

plt.style.use('fivethirtyeight') # Plot style

VLine = np.linspace(0, 6, 14)
ILine = np.linspace(0, 6, 14)
PLine = np.linspace(30, 0, 14)
# This will get replaced by measured values

fig, ax1 = plt.subplots() # Create plot object
ax2 = ax1.twinx() # Create a second y axis

Vdata = []
Pdata = []
reading = ""
# Declaring arrays that will grow

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    # Create a serial port object
except serial.SerialException:
    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
    # Try the next port incase 2 usb devices are plugged in

def checkIfCtrlC(): # Ctrl-c quitting functionality
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
        ser.close() # Close serial connection
        exit() # Kill program

date = datetime.datetime.now().strftime("%B-%d-%H-%M-%S")

with open('logs/VIVPcurves.csv', 'r') as curvesFile, \
    open(f'logs/measured-data-{date}.csv', 'w') as dataFile:


    def getChAndMeasurement(line):
        try:
            line = ser.readline().decode('utf-8')
        except UnicodeDecodeError:
            print("Retrying USB read")
            time.sleep(0.01)
            line = ser.readline().decode('utf-8')
        # Reading from USB
    
        channel = 4
        measurement = 747.747
    
        if "\x1b[2J\x1b[H" in line:
            line = line.replace("\x1b[2J\x1b[H", "")
        # Filter out screen clearing escape characters
    
        float_match = re.search(r'\d+\.\d+', line) 
        if float_match:
            measurement = float(float_match.group())
            print(f"Float {measurement}")
        # Collect floats using regular expressions
    
        int_match = re.search(r'\d+', line)
        if int_match:
            channel = int(int_match.group())
            print(f"Int {channel}")
        # Collect ints using regular expressions
        
    
    
    def animate(i):
    
        getChAndMeasurement(reading)
    
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
    
        Vdata.append(random.uniform(0, 6))
        Pdata.append(random.uniform(0, 30))
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
    
