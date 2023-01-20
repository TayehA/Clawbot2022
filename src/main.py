#cant import functions from other files/modules rip
from vex import *

#CLOCK WISE IS TRUE
#COUNTER CLOCK WISE IS FALSE

#9-12 is defining which motors are doing what

arm = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False) 
claw = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)

con = Controller()#controler
brain=Brain()

def driver_control(): 
    #loop should not break unless automonous is enabled

    while True:
        
        #button movements 
        
        if con.buttonA.pressing()==True:
            arm.set_velocity(60, PERCENT) 
            arm.spin(FORWARD)
        elif con.buttonB.pressing()==True:
            arm.set_velocity(60, PERCENT) 
            arm.spin(REVERSE)
        if con.buttonX.pressing()==True:
            claw.set_velocity(50, PERCENT)
            claw.spin(FORWARD)
        elif con.buttonY.pressing()==True:
            claw.set_velocity(50, PERCENT)
            claw.spin(REVERSE)
        else:
            arm.set_velocity(0, PERCENT)
            arm.set_stopping(HOLD) #this should make the arm stay in place
            
            pos1=con.axis3.position() 
            pos2=con.axis2.position()

            right_motor.set_velocity(pos2, PERCENT)
            left_motor.set_velocity(pos1, PERCENT)
            left_motor.spin(FORWARD)
            right_motor.spin(FORWARD)



        wait(20, MSEC) 
        #speed does not matter, it only matter how long it lasts (THAT WAS SHE SAID)




        #joystick postions
        #currently set as split controls
        #this should not be in the else stament becasuse we want to move the arm and claw in the same time
        pos1= con.axis3.position()
        pos2= con.axis2.position()
        left_motor.set_velocity(pos1)
        right_motor.set_velocity(pos2)
        left_motor.spin(REVERSE)
        right_motor.spin(REVERSE)
        






def pre_auto():

    brain.screen.clear_screen()
    brain.screen.print("Ameer is cool!")


def auto():#automonous
    #YOU CANT SET THE VELOCITY ABOVE 100% DO YOU THINK YOU CAN OVERCLOCK THIS JUSTIN?!??!?!?

    left_motor.set_velocity(100, PERCENT)
    right_motor.set_velocity(100, PERCENT)
    arm.set_velocity(60, PERCENT)
    #lifts the arm up and moves forward
    arm.spin(FORWARD)
    left_motor.spin(REVERSE)
    right_motor.spin(REVERSE)

    wait(2, SECONDS)
    #arm stops moving
    arm.stop()
    wait(4, SECONDS)
    #nothing moves after this
    left_motor.stop()
    right_motor.stop() 



Competition(driver_control, auto)
pre_auto()
