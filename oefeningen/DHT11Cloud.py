import time,board,adafruit_dht, subprocess #importeer


dhtDevice = adafruit_dht.DHT11(board.D18)   #verbind de dht11 op pin 18 en noem het dhtDevice

#temperature_c = dhtDevice.temperature   #zet de temperatuur van de DHT11 in variabele temperature_c
#luchtvochtigheid = dhtDevice.humidity   #zet de luchtvochtigheid van de DHT11 in variabele luchtvochtigheid

f=open("DHT11Cloud.csv","w")    #start met schrijven in het bestand DHT11Cloud.csv
f.write("temp,lv \n")   #schrijf in het bestand en maak een nieuwe regel
f.close()   # stop met schrijven

while True: #doe de hele tijd
    if (int(time.strftime("%S"))%5) == 0:   #als de rest 0 is als je de seconden deelt door 5 
        try:    #probeer
            temperature_c = dhtDevice.temperature   #zet de temperatuur van de DHT11 in variabele temperature_c
            luchtvochtigheid = dhtDevice.humidity   #zet de luchtvochtigheid van de DHT11 in variabele luchtvochtigheid
            f=open("thermometerCSV.csv","a")    # voeg toe aan het bestand
            f.write(f"{temperature_c},{luchtvochtigheid}\n") #tekst schrijven in het bestand
            f.close()   #sluit het bestand
            subprocess.run(["/bin/bash", "/bin/auto_push.sh"])
        except RuntimeError as error:   #tenzij er een runtime error is
            print(error.args[0])    #print de error
            continue    #ga verder
        except Exception as error:  #tenzij er een exception error is
            dhtDevice.exit()    #stop de dhtDevice
            raise error #doe de error weg