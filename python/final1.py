from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil # Needed for command message definitions
import math
import RPi.GPIO as GPIO
import time
import dronekit

connection_string = "/dev/ttyACM0,115200"
print("Connecting to...% s" % connection_string)
vehicle = connect(connection_string, wait_ready=True)

print(vehicle.mode)


print " Type: %s" % vehicle._vehicle_type
print " Armed: %s" % vehicle.armed
print " System status: %s" % vehicle.system_status.state
print " GPS: %s" % vehicle.gps_0
print " Alt: %s" % vehicle.location.global_relative_frame.alt


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
 time.sleep(1)

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
 print d0

 GPIO.output(TRIGHT, False)
 time.sleep(1)

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
 print d1

 GPIO.output(TBACK, False)
 time.sleep(1)

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
 print d2

 GPIO.output(TLEFT, False)
 time.sleep(1)

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
 print d3

 if (d0 >2 and d0 <400):
  # move back

  def send_attitude_target(self, pitch_angle = -0.5):
    msg = copter.message_factory.set_attitude_target_encode(
        0,
        0,                                         		# target system
        0,                                         		# target component
        0b00000000,                                		# type mask: bit 1 is LSB
        to_quaternion(roll_angle, pitch_angle, yaw_angle),      # q
        0,                                         		# body roll rate in radian
        0,                                         		# body pitch rate in radian
        yaw_rate,                                  		# body yaw rate in radian
        thrust)                                    		# thrust
    copter.send_mavlink(msg)


 if (d1 >2 and d1 <400):
  # move left

  def send_attitude_target(self, roll_angle=0.0, pitch_angle=0.0,
                         yaw_angle=0.0, yaw_rate=10, thrust=0.5):
    msg = copter.message_factory.set_attitude_target_encode(
        0,
        0,                                         		# target system
        0,                                         		# target component
        0b00000000,                                		# type mask: bit 1 is LSB
        to_quaternion(roll_angle, pitch_angle, yaw_angle),      # q
        0,                                         		# body roll rate in radian
        0,                                         		# body pitch rate in radian
        yaw_rate,                                  		# body yaw rate in radian
        thrust)                                    		# thrust
    copter.send_mavlink(msg)


 if (d2 >2 and d2 <400):
  #move front

  def send_attitude_target(self, roll_angle=0.0, pitch_angle=0.0,
                         yaw_angle=0.0, yaw_rate=10, thrust=0.5):
    msg = copter.message_factory.set_attitude_target_encode(
        0,
        0,                                         		# target system
        0,                                         		# target component
        0b00000000,                                		# type mask: bit 1 is LSB
        to_quaternion(roll_angle, pitch_angle, yaw_angle),      # q
        0,                                         		# body roll rate in radian
        0,                                         		# body pitch rate in radian
        yaw_rate,                                  		# body yaw rate in radian
        thrust)                                    		# thrust
    copter.send_mavlink(msg)


 if (d3 >2 and d3 <400):
  # move right
  def send_attitude_target(self, roll_angle=0.0, pitch_angle=0.0,
                         yaw_angle=0.0, yaw_rate=10, thrust=0.5):
    msg = copter.message_factory.set_attitude_target_encode(
        0,
        0,                                         		# target system
        0,                                         		# target component
        0b00000000,                                		# type mask: bit 1 is LSB
        to_quaternion(roll_angle, pitch_angle, yaw_angle),      # q
        0,                                         		# body roll rate in radian
        0,                                         		# body pitch rate in radian
        yaw_rate,                                  		# body yaw rate in radian
        thrust)                                    		# thrust
    copter.send_mavlink(msg)
 print "perfect"

GPIO.cleanup()
