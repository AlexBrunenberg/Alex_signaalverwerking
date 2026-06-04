import serial, time
ventilatorOud = -1
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
    ser.reset_input_buffer()
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
        elif len(line) == 6:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            print(len(line))
            print(line[0])
            temperature = int(line[0]+line[1])
            print(temperature)
            humidity = int(line[4]+line[5])
            print(humidity)
            time.sleep(1)
            if temperature < 31:
                ventilator = 0
            elif temperature < 39 or (temperature <= 43 and 20 < humidity < 40):
                ventilator = 84.15
            elif temperature < 56:
                ventilator = 168.3
            else:
                ventilator = 255
            if ventilatorOud != ventilator:
                print("waarde ventilator: ",ventilator)
                ser.write(f"{ventilator}".encode())
                ventilatorOud = ventilator
        else:
            print(len(line))
            print("geen juiste waarde")
            print(line)

