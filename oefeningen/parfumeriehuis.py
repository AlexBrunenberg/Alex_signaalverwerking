from gpiozero import Motor, Button # importeer modules
from time import sleep  # importeer module

motor = Motor(forward=17, backward=14, pwm=True)    # stel de pinnen in voor de motor om naar voor of achter te gaan en zet pwm aan
drukknopPlus = Button(9)    # verbindt variabele drukknopPlus met drukknop op pin 9
drukknopEnter = Button(10)  # verbindt variabele drukknopEnter met drukknop op pin 10
drukknopMin = Button(11)    # verbindt variabele drukknopMin met drukknop op pin 11
dcmotorSnelheid = 1 # maak variabele dcmotorSnelheid aan en gelijk aan 1
statusPlus = 0  # maak variabele statusPlus aan
statusEnter = 0 # maak variabele statusEnter aan
statusMin = 0   # maak variabele statusMin aan

while True: # doe altijd
    # deel 1
    if drukknopPlus.is_active and dcmotorSnelheid < 5 and statusPlus == 0:  # als drukknopPlus is ingedrukt en dcmotorSnelheid kleiner is dan 5 en statusPlus 0 is dan
        dcmotorSnelheid += 1    # doe 1 bij variabele dcmotorSnelheid
        statusPlus = 1  # verander statusPlus naar waarde 1
        print(dcmotorSnelheid)    # print de waarde van de variabele dcmotorSnelheid
    if not drukknopPlus.is_active and statusPlus == 1:  # als drukknopPlus niet is ingedrukt en statusPlus is gelijk aan 1 dan
        statusPlus = 0  # verander statusPlus naar waarde 0

    if drukknopEnter.is_active and statusEnter == 0:    # als drukknopEnter is ingedrukt en statusEnter is gelijk aan 0 dan
        motor.forward((dcmotorSnelheid-1)/4)    # laat de motor vooruit draaien op de aangegeven waarde tussen 0 en 1
        statusEnter = 1 # verander statusEnter naar 1
        print(f"Stand bevestigt: {dcmotorSnelheid}")    # print de waarde van de variabele dcmotorSnelheid
    if not drukknopEnter.is_active and statusEnter == 1:    # als drukknopEnter niet is ingedrukt en StatusEnter is gelijk aan 1 dan
        statusEnter = 0 # verander statusEnter naar 0

    if drukknopMin.is_active and dcmotorSnelheid > 1 and statusMin == 0: # als drukknopmin is ingedrukt en dcmotorSnelheid groter is dan 1 en statusMin 0 is dan
        dcmotorSnelheid -= 1    # trek 1 van variabele dcmotorSnelheid af
        statusMin = 1   # verander statusMin naar 1
        print(dcmotorSnelheid)    # print de waarde van de variabele dcmotorSnelheid
    if not drukknopMin.is_active and statusMin == 1:    # als drukknopMin niet is ingedrukt en statusMin is gelijk aan 1 dan
        statusMin = 0   # verander statusMin naar 0
    # deel 2
    
    sleep(.05)    # wacht 0.05 seconde