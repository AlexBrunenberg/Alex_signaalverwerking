import time as time, board, adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)

f=open("tempText.txt","w")
f.write("nr.   Tijd   Temp.(°C) Vochtigheid(%) \n")
f.close()
teller = 1

while True:
    if (int(time.strftime("%S"))%5) == 0:
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            tijd = time.strftime("%H:%M:%S")
            f=open("tempText.txt","a")
            f.write(f"{teller}\t{tijd}    {temperature_c}         {humidity} \n")
            f.close()
            print(time.strftime("%H:%M:%S"))
            teller +=1
        except RuntimeError as error:
            print(error.args[0])
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        time.sleep(2)

f=open("tempText.txt","w")
f.write("dit is regel 1")
f.close()

f=open("tempText.txt","a")
f.write("dit is regel 3")
f.close()

f=open("tempText.txt","r")
inhoud=f.read()
print(inhoud)
f.close