import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 16
ECHO = 18

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:

 GPIO.output(TRIG, False)
 time.sleep(0.0001)

 GPIO.output(TRIG, True)
 time.sleep(0.0001)
 GPIO.output(TRIG, False)

 a = time.time()
 b = time.time()

 while GPIO.input(ECHO)==0:
  a = time.time()


 while GPIO.input(ECHO)==1:
  b = time.time()

 x = b-a

 distance = x * 17150
 distance = round(distance, 2)

 if (distance >2 and distance <400):
  print  distance + 3,"cm"
 else:
  print distance + 3, "cm"
GPIO.cleanup()

