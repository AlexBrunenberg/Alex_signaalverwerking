from gpiozero import AngularServo   # importeer module
import board, time,adafruit_dht # importeer modules

servo = AngularServo(17, min_angle=0, max_angle=180) # definieer de servo op pin 17 en zet de minimale hoek op 0 en de maximale hoek op 180
dhtDevice = adafruit_dht.DHT11(board.D18)   # verbind de dht11 op pin 18 en noem het dhtDevice
temperatuurOud = 0  # maak variabele temperatuurOud aan

while True: # blijf altijd doorgaan
    try:    # probeer
        temperatuur = dhtDevice.temperature # zet de temperatuur van de dht11 in de variabele temperatuur
        print(temperatuur,"°C") # print de temperatuur
        if (temperatuur != temperatuurOud) and (temperatuur != None): # als de temperatuur verandert en de temperatuur een waarde heeft
            if temperatuur < 15:    # als de temperatuur kleiner is dan 15
                angle = 0   # zet 0 in de variabele angle
            elif temperatuur < 20:  # als de temperatuur kleiner is dan 20
                angle = (temperatuur - 14.9)* 36    # een formule om de temperatuur om te zetten in een angle tussen 3,6 en 180
            else:   # anders
                angle = 180 # zet 180 in de variabele angle
            servo.angle = angle # draai de servo naar de waarde van de angle
            temperatuurOud = temperatuur    # maak variabele temperatuurOud gelijk aan temperatuur
    except RuntimeError as error:   # tenzij er een runtimeError is
        print(error.args[0])    # print de error
        continue    # ga verder
    except Exception as error:  # tenzij er een exception error is
        dhtDevice.exit()    # stop de dht device
        raise error # doe de error weg
    time.sleep(2)   # wacht 2 seconden