import serial, io
from datetime import datetime
from serial import Serial

outfile='tmp/serial-temperature.tsv'

ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
   bytesize=serial.EIGHTBITS,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE)

sio = io.TextIOWrapper(
   io.BufferedRWPair(ser, ser, 1),
   encoding='ascii',newline='\r')

with open(outfile, 'a') as f: #a appends (adds) the serial-temperature file into the tmp directory
   while ser.isOpen():
      datastring = sio.readline()
      f.write(datetime.utcnow().isoformat()+ '\t' + datastring + '\n')
      f.flush()

ser.close()
