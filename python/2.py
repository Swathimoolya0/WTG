import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG1 = 16
ECHO1 = 18
TRIG2 = 19
ECHO2 = 21

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)

while True:

 GPIO.output(TRIG1, False)
 time.sleep(0.001)

 GPIO.output(TRIG1, True)
 time.sleep(0.001)
 GPIO.output(TRIG1, False)

 GPIO.output(TRIG2, False)
 time.sleep(0.001)

 GPIO.output(TRIG2, True)
 time.sleep(0.001)
 GPIO.output(TRIG2, False)

 a = time.time()
 b = time.time()
 c = time.time()
 d = time.time()

 while GPIO.input(ECHO1)==0:
  a = time.time()

 while GPIO.input(ECHO1)==1:
  b = time.time()

 while GPIO.input(ECHO2)==0:
  c = time.time()

 while GPIO.input(ECHO2)==1:
  d = time.time()


 x = b-a
 y = d-c


 distance1 = x * 17150
 distance1 = round(distance1, 2)

 distance2 = y * 17150
 distance2 = round(distance2, 2)

 if(distance1 >2 and distance1 <400) or (distance2 >2 and distance2 <400):
  print  distance1,"cm","\t",distance2,"cm"
 else:
  print distance1,"cm","\t",distance2,"cm"
GPIO.cleanup()

