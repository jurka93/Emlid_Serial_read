import serial
import time

def serial_init(port_):
    if(not(isinstance(port_, str))):
        raise ValueError('port must be string')
    ser = serial.Serial(
        port=port_,
        baudrate = 115200,
		timeout = 1
        )

    return(ser)
#example
my_ser = serial_init('COM4')

while(True):
	got_message = my_ser.readline().split()
	for elem in got_message[:5]:
		print(elem)
	time.sleep(1)
my_ser.close()
'''
x = my_ser.read()          # read one byte
if not x:
    print('there is nothing')
else:
	print(x)
	
s = my_ser.read(10)        # read up to ten bytes (timeout)
if not s:
    print('there is nothing')
else:
	print(s)
line = my_ser.readline()   # read a '\n' terminated line
if not line:
    print('there is nothing')
else:
	print(line)'''
	



