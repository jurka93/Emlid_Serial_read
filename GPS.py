import serial

def serial_init(port_, timeout):
    if(not(isinstance(port_, str))):
        raise ValueError('port must be string')
    ser = serial.Serial(
        port='COM20',
        baudrate = 115200,
        timeout=timeout
        )

    return(ser)
#example
my_ser = serial_init('COM20',1)

x = my_ser.read()          # read one byte
if not x:
    print('there is nothing')
s = my_ser.read(10)        # read up to ten bytes (timeout)
if not s:
    print('there is nothing')
line = my_ser.readline()   # read a '\n' terminated line
if not line:
    print('there is nothing')


