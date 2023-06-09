
import re # for processing text 
import time # for waiting to retry serial read

def getMeasurements(line, ser):

    data2csv = [1000, 1000, 1000]

    count = 0

    """
    Change the stuff below to not be a while loop but collects 3 lines
    and then performs list comprehensions on the lines for filtering

    """

    while count < 3: # Get 3 measurements
        try:
            line = ser.readline().decode('utf-8')
        except UnicodeDecodeError:
            print("Retrying USB read")
            time.sleep(0.01)
            line = ser.readline().decode('utf-8')
        # Reading from USB
    
        channel = 4
        measurement = 747.747
    
    
        float_match = re.search(r'\d+\.\d+', line) 
        if float_match:
            measurement = float(float_match.group())
        # Collect floats using regular expressions
    
        int_match = re.search(r'\d+', line)
        if int_match:
            channel = int(int_match.group())
        # Collect ints using regular expressions

        if channel < 4:
            data2csv[channel] = measurement
        # Make sure its a valid channel

        count += 1

    return data2csv
