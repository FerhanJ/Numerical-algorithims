import math

#Algorithim that calculates the integral of f(x) using the 
#trapeziodal rule until the deisred accuracy is achieved.
#After each iteration the number of slices N doubles

N = 1 # initial number of slices
a = 0 # define interval [a,b] for our integral
b = 10
error = 10**-5
limit = 100 # number of loops to run before stopping the programme
# define function to integrate
def f(x):
    return math.sin(x**2) + math.sin(x**7)

def trapInt(a, b, N): # integrate f(x) in interval [a,b] with N trapeziums
	h = (b - a)/N
	I = .5*h*(f(a) + f(b))
	for k in range(1,N + 1):
		I += h*f(a + k*h)
	return I	


I = [0,0]
I[0] = trapInt(a, b, N)
count = 0

while True:
	count += 1 
	newEst = 0
	N = 2*N
	h = (b - a)/N

	#calculate new integral after doubling N
	for k in range(1,N,2):
		newEst += h*f(a + k*h)
	oldEst = .5*I[0]
	I[1] = oldEst + newEst

	#calculate accuracy of our integral
	accuracy = (1/3)*abs(I[0] - I[1])
	#print feedback
	print("Accuracy is " + str(accuracy))
	print("Integral is " + str(I[1]) + " with " +str(N) + " slices")
	
	#if our estimate is accurate enough then stop 
	if accuracy < abs(error):
		print("converged in " + str(count) + " loops")
		break
	#if we dont converge in the limit then stop
	if count > limit:
		print("failed to converge to the required error within " + str(limit) + " steps")
		break
	
	#turn our new estimate into the old estimate	
	I[0] = I[1]
