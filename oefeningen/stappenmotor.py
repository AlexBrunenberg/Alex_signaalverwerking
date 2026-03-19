from RpiMotorLib import RpiMotorLib # importeer een module

motor = RpiMotorLib.BYJMotor("motor", "28BYJ")  # maak de motor aan en stel het type motor in
GpioPins = [18,23,24,25]    # maak een lijst aan met de pinnen
afstand = float(input("Hoeveel mm wil je verplaatsen: "))*512/3 # vraag aan de gebruiker hoeveel afstand dat die wilt draaien, en vermenigvuldig het met 512 en deel het door 3 want 3mm/toer
motor.motor_run(GpioPins,.005,afstand,False,False,"full",.05)   # laat de motor de afstand draaien