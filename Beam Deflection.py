import sympy as sp
from scipy.integrate import quad
#input given values

E = int(float(input("enter modulus value: ")))
I = int(float(input("enter inertia about z axis: ")))
forceone = int(input("enter value of first force: "))
forcetwo = int(input("enter value of second force: "))

#input distances

Distance_B_from_A = int(input("Input the distance from point B to point A: "))
Distance_forceone_from_A = int(input("Input the distance from point forceone to point A: "))
Distance_forcetwo_from_A = int(input("Input the distance from point forcetwo to point A: "))

#Forces for point A and B

B = int(forceone*Distance_forceone_from_A+forcetwo*Distance_forcetwo_from_A)/Distance_B_from_A
A = int(forceone+forcetwo-B)

#double integration method

print("this is B "+str(B)+" this is A "+str(A))


x = sp.Symbol('x')

newint =sp.integrate(-((B*(x-(Distance_B_from_A-Distance_B_from_A)))-(forcetwo*(x-(Distance_B_from_A-Distance_forcetwo_from_A)))-(forceone*(x-(Distance_B_from_A-Distance_forceone_from_A)))),x)


secondint = sp.integrate(newint,(x,0,4))


final_answer = secondint/(E*I)

print(final_answer)