from gpiozero import Motor, Button, AngularServo # importeer modules
from time import sleep  # importeer module
import adafruit_dht, board # importeer modules

motor = Motor(forward=17, backward=14, pwm=True)    # stel de pinnen in voor de motor om naar voor of achter te gaan en zet pwm aan
drukknopPlus = Button(9)    # verbindt variabele drukknopPlus met drukknop op pin 9
drukknopEnter = Button(10)  # verbindt variabele drukknopEnter met drukknop op pin 10
drukknopMin = Button(11)    # verbindt variabele drukknopMin met drukknop op pin 11
dcmotorSnelheid = 1 # maak variabele dcmotorSnelheid aan en gelijk aan 1
statusPlus = 0  # maak variabele statusPlus aan
statusEnter = 0 # maak variabele statusEnter aan
statusMin = 0   # maak variabele statusMin aan

dht = adafruit_dht.DHT11(board.D18)   # verbind de dht11 op pin 18 en noem het dht
servo = AngularServo(27, min_angle=0, max_angle=180)   # verbind de servo op pin 27 en noem het servo
hoek = 0    # maak variabele hoek aan
hoekOud = 0 # maak variabele hoekOud aan

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
    try:    # probeer
        luchtvochtigheid = dht.humidity # zet de luchtvochtigheid van de dht11 in de variabele luchtvochtigheid
        print(luchtvochtigheid) # print de luchtvochtigheid
        if luchtvochtigheid != None:    # als de luchtvochtigheid niet niks is dan
            if luchtvochtigheid <= 40:  # als de luchtvochtigheid kleiner of gelijk aan 40 is dan
                hoek = 10   # maak hoek gelijk aan 10
            elif luchtvochtigheid <= 60:    # anders  als de luchtvochtgheid kleiner of gelijk aan 60 is dan
                hoek = 45   # maak hoek gelijk aan 45
            elif luchtvochtigheid <= 75:    # anders  als de luchtvochtigheid kleiner of gelijk aan 75 is dan
                hoek = 90   # maak hoek gelijk aan 90
            elif luchtvochtigheid <= 90:    # anders als de luchtvochtigheid kleiner of gelijk aan 90 is dan 
                hoek = 135  # maak hoek gelijk aan 135
            else:   # anders
                hoek = 170  # maak hoek gelijk aan 170
        servo.angle = hoek  # zet de servo op het aantal graden dat variabele hoek aangeeft
    except RuntimeError as error:   # tenzij er een runEimeError is
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])    # print de error
        continue    # ga verder
    except Exception as error:  # tenzij er een exception error is
        dht.exit()    # stop de dht device
        raise error # doe de error weg
    sleep(.05)    # wacht 0.05 seconde