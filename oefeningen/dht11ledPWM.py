import board, time,adafruit_dht # importeer modules
from gpiozero import RGBLED # importeer modules

led = RGBLED(red = 10, green = 11, blue = 9) # definieer de LED
dhtDevice = adafruit_dht.DHT11(board.D18)   #verbind de dht11 op pin 18 en noem het dhtDevice
lijst = [[255,0,0] ,[205,38,38] ,[205,55,0] ,[250,128,114] ,[238,149,114] ,[255,127,0],[205,133,0],[238,173,14],[238,221,130] ,[205,205,0] ,[255,246,143] ,[124,252,0] ,[0,255,0] ,[78,238,148] ,[0,245,255] ,[151,255,255] ,[0,255,255] ,[135,206,250] ,[0,191,255] ,[30,144,255] ,[0,0,255]]  # zet alle 21 rgb waardes in een lijst

while True: # blijf altijd doorgaan
    try:    # probeer
        temperatuur = dhtDevice.temperature # zet de temperatuur van de dht11 in de variabele temperatuur
        print(temperatuur,"°C") # print de temperatuur
        if temperatuur != None: # als de temperatuur een waarde heeft
            lijstNummer = int(round((temperatuur/2),0)) # deel de temperatuur door 2, rond het af tot een geheel getal, maak er een integer van en zet het in de variabele lijstNummer
            lijstNummer = -lijstNummer -1   # maak de waarde van lijstNummer negatief en trek er 1 van af
            led.color = ((lijst[lijstNummer][0])/255, (lijst[lijstNummer][1])/255, (lijst[lijstNummer][2])/255)   # zet de 3 waardes van de lijst in de rgb led en deel ze door 255
    except RuntimeError as error:   # tenzij er een runEimeError is
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])    # print de error
        continue    # ga verder
    except Exception as error:  # tenzij er een exception error is
        dhtDevice.exit()    # stop de dht device
        raise error # doe de error weg
    time.sleep(2)   # wacht 2 seconden