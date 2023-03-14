import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import keyboard

def quitWindow():
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('c'):
        plt.close()

SIZE = 10

plt.style.use('fivethirtyeight')

# This will get replaced by real values
VLine = np.linspace(0, 6, 14)
ILine = np.linspace(0, 6, 14)
PLine = np.linspace(30, 0, 14)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

Vdata = []
Pdata = []


def animate(i):
    ax1.cla()
    ax2.cla()
    # Clear each axes

    ax1.plot(VLine, ILine, linestyle='--', linewidth=1.5)
    ax1.set_xlabel('Voltage (V)')
    ax1.set_ylabel('Current (A)')

    ax2.plot(VLine, PLine, linestyle='--', linewidth=1.5)
    ax2.set_ylabel('Power (W)', labelpad=15)
    ax2.yaxis.set_label_coords(1.075, 0.5)

    Vdata.append(random.uniform(0, 6))
    Pdata.append(random.uniform(0, 30))

    ax2.scatter(Vdata[-(SIZE+1):-1], Pdata[-(SIZE+1):-1], marker='o', color='red')
    ax2.scatter(Vdata[-1], Pdata[-1], marker='o', color='blue')

    quitWindow()


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()


