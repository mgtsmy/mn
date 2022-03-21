import RPi.GPIO as P
import time  
P.setmode(P.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

for items in dac:
    P.setup(items, P.OUT)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    for i in range(255):
        P.output(dac, dec2bin(i))
        time.sleep(0.1)
        i += 1
finally:
    dac = [0, 0, 0, 0, 0, 0, 0, 0]
    P.cleanup()