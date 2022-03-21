import RPi.GPIO as P  
P.setmode(P.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]

for items in dac:
    P.setup(items,P.OUT)

def dlb(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


try:
    while True:
        print("введите число от 0 до 255")
        n = int(input())
        P.output(dac, dlb(n))
        print("V =", round(3.3/256*n, 4))

except ArithmeticError:
    n = None

finally:
    dac = [0, 0, 0, 0, 0, 0, 0, 0]
    P.cleanup()