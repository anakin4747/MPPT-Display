import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial


SIZE = 10
# Practically a define but its not C so its a variable

plt.style.use('fivethirtyeight')

VLine = np.linspace(0, 6, 14)
ILine = np.linspace(0, 6, 14)
PLine = np.linspace(30, 0, 14)
# This will get replaced by real values

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

Vdata = []
Pdata = []


def animate(i):
    ax1.cla()
    ax2.cla()
    # Clear each axes

    ax1.plot(VLine, ILine, linestyle='--', linewidth=1.5)
    # Setting line weight and style
    ax1.set_xlabel('Voltage (V)')
    ax1.set_ylabel('Current (A)')

    ax2.plot(VLine, PLine, linestyle='--', linewidth=1.5)
    # Setting line weight and style
    ax2.set_ylabel('Power (W)', labelpad=15)
    # Label kept over lapping the ax1.ylabel - this fixed it
    ax2.yaxis.set_label_coords(1.075, 0.5)

    Vdata.append(random.uniform(0, 6))
    Pdata.append(random.uniform(0, 30))
    # Update data points

    ax2.scatter(Vdata[-(SIZE+1):-1], Pdata[-(SIZE+1):-1], \
            marker='o', color='red')
    # Real-time data except the most recent data point

    ax2.scatter(Vdata[-1], Pdata[-1], marker='o', color='blue')
    # Real-time most recent data point


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()


