from gpiozero import LEDBoard # importeer LEDBoard
from time import sleep  # importeer sleep

leds = LEDBoard(4,17,27,22,10,9,5,6)    # gebruik de functie LEDBoard en zet er pinnen in van leds

def knight_rider_links(leds):   # maak de functie knight_rider_links aan en vraag voor een input
    for led in range(0,7,1):    # maak led gelijk aan 0 en voeg er iedere keer 1 bij tot 7
        leds[led].on()  # maak index led van leds aan
        sleep(0.1)  # wacht 100ms
        leds[led].off() # maak index led van leds uit
def knight_rider_rechts(leds):  # maak de functie knight_rider_rechts aan en vraag voor een input
    for led in range(7,0,-1):  # maak led gelijk aan 7 en trek er iedere keer 1 af tot 0
        leds[led].on() # maak index led van leds aan
        sleep(0.1)  # wcht 100ms
        leds[led].off()    # maak index led van leds uit
while True: # blijf de hele tijd doorgaan
    knight_rider_links(leds)    # voer de functie uit en geef waarde leds mee
    knight_rider_rechts(leds)   # voer de functie uit en geef waarde leds mee