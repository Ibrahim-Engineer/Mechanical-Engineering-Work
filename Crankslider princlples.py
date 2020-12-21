import numpy as np
import pandas as pd
import math
x = int(float(input("enter length of crank arm. If value is unknown enter 0: ")))
if x == 0:
    angleint = int(float(input("enter angle of crank arm: ")))

    a = int(float(input("enter length of arm: ")))

    b = int(float(input("enter distance of slider from origin: ")))
elif x > 0:

	y = int(float(input("enter length of arm: ")))

	z = int(float(input("enter distance of slider from origin: ")))


	######angle between crank arm and plane in which distance of slider from origin is found for theta 2########
	theta2 = 180 -(math.acos((y*y-x*x-z*z)/(2*x*z)))*(180/(math.pi))
	print(theta2)
	print("angle between crank arm and plane in which distance of slider from origin")

	#######theta3

	theta3 = 180 -(math.acos((z*z-x*x-y*y)/(2*x*y)))*(180/(math.pi))
	print(theta3)
	print("angle between the crank arm and arm")

	#######theta4

	theta4 = 180 -(math.acos((x*x-z*z-y*y)/(2*z*y)))*(180/(math.pi))
	print(theta4)

	print("angle between arm and plane in which the distance of the slider from the origin is found")
###########################################velocity###########################################
	#############################initial velocity of the crank arm##########################

	int_v0 = int(float(input("enter initail velocity of crank arm: ")))

	print(int_v0)
	print("initial velocity of crank arm")

	########################velocity of arm######################

	v1 = math.sin(theta4 -90)*(int_v0/math.sin(theta2-90))
	print(v1)
	print("velocity of arm")

	#########################veloctiy of slider########################


	vslider = math.sin(180+(theta2-90)+(theta4-90))*(int_v0/math.sin(theta2-90))
	print(vslider)
	print("velocity of slider")


elif x < 0:
	print("crank length not possible")



