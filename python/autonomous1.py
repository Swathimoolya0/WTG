from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time

connection_string = "/dev/ttyACM0,115200"
print("Connecting to...% s" % connection_string)
vehicle = connect(connection_string, wait_ready=True)

# Function to arm and then takeoff to a user specified altitude
def arm_and_takeoff(aTargetAltitude):

  print "Basic pre-arm checks"
  # Don't let the user try to arm until autopilot is ready
  while not vehicle.is_armable:
    print " Waiting for vehicle to initialise..."
    time.sleep(1)

  print "Arming motors"
  # Copter should arm in GUIDED mode
  vehicle.mode    = VehicleMode("GUIDED")
  vehicle.armed   = True

  while not vehicle.armed:
    print " Waiting for arming..."
    time.sleep(1)

  print "Taking off!"
  vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

  # Check that vehicle has reached takeoff altitude
  while True:
    print " Altitude: ", vehicle.location.global_relative_frame.alt 
    #Break and return from function just below target altitude.        
    if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
      print "Reached target altitude"
      break
    time.sleep(1)

# Initialize the takeoff sequence to 7m
arm_and_takeoff(7)
print("Take off complete")
# Hover for 10 seconds
time.sleep(10)
print("Now let's land")
vehicle.mode = VehicleMode("LAND")
# Close vehicle object
vehicle.close()
