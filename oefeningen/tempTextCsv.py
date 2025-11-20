import time as time, board, adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)

f=open("tempText.csv","w")
f.write("nr,tijd,tempDHT11,tempDS18B20,gemiddeldeTemp \n")
f.close()
teller = 1

while True:
    if (int(time.strftime("%S"))%5) == 0:
        try:
            temperature_c = dhtDevice.temperature
            tijd = time.strftime("%H:%M:%S")
            f=open("tempText.csv","a")
            f.write(f"{teller},{tijd},{temperature_c}\n")
            f.close()
            teller +=1
        except RuntimeError as error:
            print(error.args[0])
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        time.sleep(2)