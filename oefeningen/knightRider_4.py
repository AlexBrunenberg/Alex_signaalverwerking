from gpiozero import LEDBoard # importeer LEDBoard
from time import sleep  # importeer sleep

leds = LEDBoard(4,17,27,22,10,9,5,6)    # gebruik de functie LEDBoard en zet er pinnen in van leds
led = 0 # maak variabele led aan en maak het gelijk aan 0
def aan_uit(led):   # maak functie aan_uit aan en vraag een input
    leds[led].on()  # zet index led van leds aan
    sleep(0.1)  # wacht 100ms
    leds[led].off() # zet index led van leds uit
    

while True: # blijf de hele tijd doorgaan
    while led != 8: # zolang led niet gelijk is aan 8
        aan_uit(led)    # gebruik functie aan_uit en geef input led mee
        led += 1    # doe 1 bij led
    led = 6 # maak led gelijk aan 6
    while led != 0: # zolang led niet gelijk is aan 0
        aan_uit(led)    # gebruik functie aan_uit en geef input led mee
        led = led - 1   # doe 1 van led af
