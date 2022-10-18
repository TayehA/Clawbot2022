

from vex import *

#CLOCK WISE IS TRUE
#COUNTER CLOCK WISE IS FALSE

arm = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
claw = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
con = Controller()

def allah():
    while True:
        arm.set_velocity(60, PERCENT)
        if con.buttonA.pressing()==True:
            arm.spin(FORWARD)
        elif con.buttonB.pressing()==True:
            arm.spin(REVERSE)
        else:
            arm.stop()
        pos1= con.axis3.position()
        pos2= con.axis2.position()
        left_motor.set_velocity(pos1)
        right_motor.set_velocity(pos2)
        left_motor.spin(FORWARD)
        right_motor.spin(FORWARD)

Thread(allah)