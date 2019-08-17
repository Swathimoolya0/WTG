import math,time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TFRONT = 16
EFRONT = 18
TRIGHT = 11
ERIGHT = 12
TBACK  = 13
EBACK  = 15
TLEFT  = 19
ELEFT  = 21

GPIO.setup(TFRONT,GPIO.OUT)
GPIO.setup(EFRONT,GPIO.IN)
GPIO.setup(TRIGHT,GPIO.OUT)
GPIO.setup(ERIGHT,GPIO.IN)
GPIO.setup(TBACK,GPIO.OUT)
GPIO.setup(EBACK,GPIO.IN)
GPIO.setup(TLEFT,GPIO.OUT)
GPIO.setup(ELEFT,GPIO.IN)

while True:

 GPIO.output(TFRONT, False)
 time.sleep(0.0001)

 GPIO.output(TFRONT, True)
 time.sleep(0.0001)
 GPIO.output(TFRONT, False)

 a = time.time()
 b = time.time()

 while GPIO.input(EFRONT)==0:
  a = time.time()


 while GPIO.input(EFRONT)==1:
  b = time.time()

 x = b-a

 d0 = x * 17150
 d0 = round(d0, 0)





 GPIO.output(TRIGHT, False)
 time.sleep(0.0001)

 GPIO.output(TRIGHT, True)
 time.sleep(0.0001)
 GPIO.output(TRIGHT, False)

 c = time.time()
 d = time.time()

 while GPIO.input(ERIGHT)==0:
  c = time.time()

 while GPIO.input(ERIGHT)==1:
  d = time.time()

 y = d-c

 d1 = y * 17150
 d1 = round(d1, 0)




 GPIO.output(TBACK, False)
 time.sleep(0.0001)

 GPIO.output(TBACK, True)
 time.sleep(0.0001)
 GPIO.output(TBACK, False)

 e = time.time()
 f = time.time()

 while GPIO.input(EBACK)==0:
  e = time.time()


 while GPIO.input(EBACK)==1:
  f = time.time()

 z = f-e

 d2 = z * 17150
 d2 = round(d2, 0)



 GPIO.output(TLEFT, False)
 time.sleep(0.0001)

 GPIO.output(TLEFT, True)
 time.sleep(0.0001)
 GPIO.output(TLEFT, False)

 g = time.time()
 h = time.time()

 while GPIO.input(ELEFT)==0:
  g = time.time()

 while GPIO.input(ELEFT)==1:
  h = time.time()

 w = h-g
 d3 = w * 17150
 d3 = round(d3, 0)

 if d0 <400:
  print "front"
 
 if d1 <400:
  print "\tright"

 if d2 <400:
  print "\t" "\t" "back"

 if d3 <400:
  print "\t\t\tleft"

GPIO.cleanup()
