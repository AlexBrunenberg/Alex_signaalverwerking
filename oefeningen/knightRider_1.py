from gpiozero import LEDBoard # importeer LEDBoard
from time import sleep  # importeer sleep

leds = LEDBoard(4,17,27,22,10,9,5,6)    # gebruik de functie LEDBoard en zet er pinnen in van leds
while True: # blijf de hele tijd doorgaan
    for led in range(0,7,1):    # maak led gelijk aan 0 en voeg er iedere keer 1 bij tot 7
        leds[led].on()  # # maak index led van leds aan
        sleep(0.1)  # wacht 100ms
        leds[led].off() # maak index led van leds uit
    for led1 in range(7,0,-1):  # maak led gelijk aan 7 en trek er iedere keer 1 af tot 0
        leds[led1].on() # maak index led van leds aan
        sleep(0.1)  # wacht 100ms
        leds[led1].off()    # maak index led van leds uit