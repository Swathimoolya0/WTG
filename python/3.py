import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG1 = 19
ECHO1 = 21
TRIG2 = 16
ECHO2 = 18
TRIG3 = 11
ECHO3 = 12

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)

while True:

 GPIO.output(TRIG1, False)
 time.sleep(1)

 GPIO.output(TRIG1, True)
 time.sleep(1)
 GPIO.output(TRIG1, False)

 GPIO.output(TRIG2, False)
 time.sleep(1)

 GPIO.output(TRIG2, True)
 time.sleep(1)
 GPIO.output(TRIG2, False)

 GPIO.output(TRIG3, False)
 time.sleep(1)

 GPIO.output(TRIG3, True)
 time.sleep(1)
 GPIO.output(TRIG3, False)

 a = time.time()
 b = time.time()
 c = time.time()
 d = time.time()
 e = time.time()
 f = time.time()

 while GPIO.input(ECHO1)==0:
  a = time.time()

 while GPIO.input(ECHO1)==1:
  b = time.time()

 while GPIO.input(ECHO2)==0:
  c = time.time()

 while GPIO.input(ECHO2)==1:
  d = time.time()

 while GPIO.input(ECHO3)==0:
  e = time.time()

 while GPIO.input(ECHO3)==1:
  f = time.time()


 x = b-a
 y = d-c
 z = f-e

 distance1 = x * 17150
 distance1 = round(distance1, 2)

 distance2 = y * 17150
 distance2 = round(distance2, 2)

 distance3 = z * 17150
 distance3 = round(distance3, 2)


 if (distance1 >2 and distance1 <400) or (distance2 >2 and distance2 <400) or (distance3 >2 and distance3 <400) :
  print  distance1,"cm","\t",distance2,"cm","\t",distance3
 else:
  print distance1,"m","\t",distance2,"m","\t",distance3,"m"
GPIO.cleanup()

