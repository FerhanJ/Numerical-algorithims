import math
#VARIABLES
a = -math.pi # define the limit [a,b] for our integral
b = math.pi
N = 100 # number of slices
h = (b - a)/N # width, h, per slice

# define function to integrate
def f(x):
    return math.exp(-x**2)
print("With " + str(N) + " segments")

#====TRAPEZIUM RULE====
I = 0 #total integral
def area(x): # find area of the xth slice
    return .5*h*(f(a + (x - 1)*h) + f(a + x*h)) 
for k in range(1,N+1): # sum over all N slices to find I
    I += area(k)
print("Trapezium rule: I = " +str(I))

#====SIMPSON RULE====
I = f(a) + f(b) #total integral
for k in range(1,N,2):
    I += 4*f(a + k*h)
for k in range(2,N,2):
    I += 2*f(a + k*h)
I = (1/3)*h*I
print("Simpson rule: I =" +str(I))