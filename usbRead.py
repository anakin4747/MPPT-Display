import serial

# create a serial port object
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

reading = ""

# read data from the serial port
while True:
    reading = ser.readline()
    

    nextChannel = reading[-3:-1].decode('utf-8')

    if nextChannel == "C0":
        # Channel 2 Voltage reading at current 
        # 200mV/A
        print(reading[1:-3].decode('utf-8'))

    elif nextChannel == "C1":
        # Channel 0 Battery level x 10
        print(reading[1:-3].decode('utf-8'))
    elif nextChannel == "C2":
        # Channel 1 Voltage x 10
        print(reading[1:-3].decode('utf-8'))


    # Voltage divider by 2
    
    # print(reading[-3:-1].decode('utf-8'))

# close the serial port
ser.close()
