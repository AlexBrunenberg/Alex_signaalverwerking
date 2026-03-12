from gpiozero import Motor, MCP3008 # importeer modules
from time import sleep  # importeer module

pot = MCP3008(channel=0)    # maak de potentiometer gelijk aan channel 0 van de MCP3008
motor = Motor(forward=17, backward=14, pwm=True)    # stel de pinnen in voor de motor om naar voor of achter te gaan en zet pwm aan
while True: # doe altijd
    motor.forward(pot.value)    # laat de motor vooruit draaien op de snelheid van de waarde van de potentiometer
    print(pot.value)    # print de waarde van de potentiometer
    sleep(1)    # wacht 1 seconde