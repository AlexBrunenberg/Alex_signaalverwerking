import time,board,adafruit_dht  #importeer
import RPi.GPIO as GPIO #importeer
from w1thermsensor import W1ThermSensor #importeer

GPIO.setmode(GPIO.BCM)  #De gpio in modus bcm zetten
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP) # maak van pin 4 een pull up
dhtDevice = adafruit_dht.DHT11(board.D18)   #verbind de dht11 op pin 18 en noem het dhtDevice
sensor = W1ThermSensor()    #zet de waarde van W1ThermSensor in variabele sensor


temperature_c = dhtDevice.temperature   #zet de temperatuur van de DHT11 in variabele temperature_c
temperature_in_celcius = sensor.get_temperature()   # zet de temperatuur van de DS18B20 shield in variabele temperature_in_celsius
gemiddelde_temp = (temperature_in_celcius + temperature_c) /2   #bereken de gemmidelde temperatuur van de 2 sensoren en zet het in variabele gemmidelde_temp

f=open("thermometerCSV.csv","w")    #start met schrijven in het bestand thermometerCSV.csv
f.write("datum,tijd,DHT11,DS18B20,gemiddeldeTemp \n")   #schrijf in het bestand en maak een nieuwe regel
f.close()   # stop met schrijven

while True: #doe de hele tijd
    if (int(time.strftime("%S"))%5) == 0:   #als de rest 0 is als je de seconden deelt door 5 
        try:    #probeer
            datum = time.strftime("%Y-%m-%d")   #zet de datum in variabele datum
            tijd = time.strftime("%H:%M:%S")    #zet de tijd in variabele tijd
            temperature_c = dhtDevice.temperature   #zet de temperatuur van de DHT11 in variabele temperature_c
            temperature_in_celcius = sensor.get_temperature()   #zet de temperatuur van de DS18B20 shield in variabele temperature_in_celsius
            gemiddelde_temp = (temperature_in_celcius + temperature_c) /2   #bereken de gemmidelde temperatuur van de 2 sensoren en zet het in variabele gemmidelde_temp
            f=open("thermometerCSV.csv","a")    # voeg toe aan het bestand
            f.write(f"{datum},{tijd},{temperature_c},{temperature_in_celcius},{gemiddelde_temp}\n") #tekst schrijven in het bestand
            f.close()   #sluit het bestand
        except RuntimeError as error:   #tenzij er een runtime error is
            print(error.args[0])    #print de error
            time.sleep(2.0) #wacht 2 seconden
            continue    #ga verder
        except Exception as error:  #tenzij er een exception error is
            dhtDevice.exit()    #stop de dhtDevice
            raise error #doe de error weg