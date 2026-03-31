from gpiozero import Motor, Button # importeer modules
from time import sleep  # importeer module

motor = Motor(forward=17, backward=14, pwm=True)    # stel de pinnen in voor de motor om naar voor of achter te gaan en zet pwm aan
drukknopPlus = Button(9)
drukknopEnter = Button(10)
drukknopMin = Button(11)
dcmotorSnelheid = 1
statusPlus = 0
statusEnter = 0
statusMin = 0

while True: # doe altijd
    if drukknopPlus.is_active and dcmotorSnelheid < 5 and statusPlus == 0:
        dcmotorSnelheid += 1
        statusPlus = 1
        print(dcmotorSnelheid)    # print de waarde van de variabele dcmotorSnelheid
    if not drukknopPlus.is_active and statusPlus == 1:
        statusPlus = 0

    if drukknopEnter.is_active and statusEnter == 0:
        #motor.forward((dcmotorSnelheid-1)/4)    # laat de motor vooruit draaien op de aangegeven waarde
        statusEnter = 1
        print(f"Stand bevestigt: {dcmotorSnelheid}")    # print de waarde van de variabele dcmotorSnelheid
    if not drukknopEnter.is_active and statusEnter == 1:
        statusEnter = 0

    if drukknopMin.is_active and dcmotorSnelheid > 1 and statusMin == 0:
        dcmotorSnelheid -= 1
        statusMin = 1
        print(dcmotorSnelheid)    # print de waarde van de variabele dcmotorSnelheid
    if not drukknopMin.is_active and statusMin == 1:
        statusMin = 0
    sleep(.05)    # wacht 0.05 seconde