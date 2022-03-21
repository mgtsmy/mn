import RPi.GPIO as P
P.setmode(P.BCM)
P.setup(22, P.OUT)
PWM = P.PWM(22, 1000)
PWM.start(0)
try:
    while True:
        a=int(input())
        PWM.ChangeDutyCycle(a)
        print((a*3.3)/100)
finally:
    P.output(22, 0)
    P.cleanup()