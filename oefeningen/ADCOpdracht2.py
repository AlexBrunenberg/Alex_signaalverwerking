import board, time, adafruit_dht    # importeer modules
from gpiozero import MCP3008, LED # importeer een module

dhtDevice = adafruit_dht.DHT11(board.D18)   #verbind de dht11 op pin 18 en noem het dhtDevice

adc = MCP3008(channel=0)  # maak een MCP3008 object op kanaal 0
groeneLed = LED(16) #verbind de groene led met pin 16
oranjeLed = LED(20) #verbind de oranje led met pin 20
rodeLed = LED(21)   #verbind de rode led met pin 21

f=open("ADCOpdracht2.csv","w")    #start met schrijven in het bestand thermometerCSV.csv
f.write("datum,tijd,DHT11(°C),TMP36(°C),verschilwaarde(°C) \n")   #schrijf in het bestand en maak een nieuwe regel
f.close()   # stop met schrijven

oudeTijd = 0    #maak variabel oudeTijd gelijk aan 0

while True: #doe de hele tijd
    tijd = time.strftime("%H:%M:%S")    #zet de tijd in variabele tijd
    if (tijd != oudeTijd) and ((int(time.strftime("%S"))%5) == 0):   #als de rest 0 is als je de seconden deelt door 5 
        try:    #probeer
            groeneLed.off() #zet de groene led uit
            oranjeLed.off() #zet de oranje led uit
            datum = time.strftime("%Y-%m-%d")   #zet de datum in variabele datum
            tijd = time.strftime("%H:%M:%S")    #zet de tijd in variabele tijd
            oudeTijd = tijd #sla de tijd op in variabele oudeTijd
            dht11Temp = dhtDevice.temperature   #zet de temperatuur van de DHT11 in variabele dht11Temp
            tmp36Temp = (adc.value * 3.3 - 0.5) * 100   # zet de waarde van de TMP36 om naar graden Celsius
            if (dht11Temp != None) or (tmp36Temp != None):  #als een van de 2 temp sensoren geen waarde krijgt
                verschil_temp = abs(dht11Temp - tmp36Temp)   # bereken het verschil tussen de 2 temperaturen
                if verschil_temp >= 2:  #als het verschil groter is dan 2
                    oranjeLed.on()  #zet de oranje led aan
                else:   #anders
                    groeneLed.on()  #zet de groene led aan
                f=open("ADCOpdracht2.csv","a")    # voeg toe aan het bestand
                f.write(f"{datum},{tijd},{dht11Temp},{tmp36Temp},{verschil_temp}\n") #tekst schrijven in het bestand
                f.close()   #sluit het bestand
                rodeLed.off()   #zet de rode led uit
            else:
                rodeLed.on()    #zet de rode led aan
        except RuntimeError as error:   #tenzij er een runtime error is
            print(error.args[0])    #print de error
            continue    #ga verder
        except Exception as error:  #tenzij er een exception error is
            dhtDevice.exit()    #stop de dhtDevice
            raise error #gooi de error weg