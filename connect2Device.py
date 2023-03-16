import serial

def connect2USB():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        # Create a serial port object

    except (FileNotFoundError, serial.SerialException):
        try:
            ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
            # Try the next port incase 2 usb devices are plugged in

        except (FileNotFoundError, serial.SerialException):
            print("\nPlug in device\n")
            exit()

    return ser
