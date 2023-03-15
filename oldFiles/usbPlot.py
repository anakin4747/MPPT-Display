import serial
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

xs = []
ys = []

index = count()

# create a serial port object
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

reading = ""

def animate(i):
    reading = ser.readline()

    xs.append(next(index))
    ys.append(random.randint(0, 5))
    # ys.append(reading[1:-1].decode('utf-8'))

    plt.cla()
    plt.plot(xs, ys)


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()


# close the serial port
ser.close()

