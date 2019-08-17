import math
import time

import dronekit

copter = dronekit.connect('udp:192.168.1.243:14550', wait_ready=True)


def send_attitude_target(self, roll_angle=0.0, pitch_angle=0.0,
                         yaw_angle=0.0, yaw_rate=10, thrust=0.5):
    msg = copter.message_factory.set_attitude_target_encode(
        0,
        0,                                         # target system
        0,                                         # target component
        0b00000000,                                # type mask: bit 1 is LSB
        to_quaternion(roll_angle, pitch_angle, yaw_angle),    # q
        0,                                         # body roll rate in radian
        0,                                         # body pitch rate in radian
        yaw_rate,                                  # body yaw rate in radian
        thrust)                                    # thrust
    copter.send_mavlink(msg)


def to_quaternion(self, roll=0.0, pitch=0.0, yaw=0.0):
    """Convert degrees to quaternions."""
    t0 = math.cos(yaw * 0.5)
    t1 = math.sin(yaw * 0.5)
    t2 = math.cos(roll * 0.5)
    t3 = math.sin(roll * 0.5)
    t4 = math.cos(pitch * 0.5)
    t5 = math.sin(pitch * 0.5)
    w = t0 * t2 * t4 + t1 * t3 * t5
    x = t0 * t3 * t4 - t1 * t2 * t5
    y = t0 * t2 * t5 + t1 * t3 * t4
    z = t1 * t2 * t4 - t0 * t3 * t5
    return [w, x, y, z]


while True:
    if(copter and copter.mode == dronekit.VehicleMode("GUIDED")):
        send_attitude_target(0,  # roll
                             0,  # pitch
                             0,  # yaw_angle
                             0,  # yaw_rate
                             0.5)  # thrust
        print("attitude command sent")
    time.sleep(0.1)
