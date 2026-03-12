from gpiozero import Motor, MCP3008
from time import sleep

pot = MCP3008(channel=0)
motor = Motor(forward=4, backward=14)
while True:
    motor.forward()
    print(pot.value)
    sleep(5)
    motor.backward()
    print(pot.value)
    sleep(5)