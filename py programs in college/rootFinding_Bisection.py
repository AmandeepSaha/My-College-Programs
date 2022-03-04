# python program to find root: Bisection Method
# Tof ind root of x*x - 4*x - 10 = 0
import numpy as np
a = float(input('Enter your value for \'a\':\t'))
b = float(input('Enter your value for \'b\':\t'))
acct = 0.0000001
def f(x):
	return x*x*x - 2*x - 2
def b(a,b,acct):
	xl = a
	xh = b
	while np.abs(xl-xh)>=acct:
		c = (xl - xh)/2.0
		if np.abs(f(c)) <= acct:
			break
		elif f(c)*f(xl)<0:
			xh = c
		else:
			xl = c
	return c
if f(a)*f(b) > 0:
	print('Intial values do not enclose any root')
elif np.abs(f(a))<= acct:
	print('The root is:',a)
elif np.abs(f(b))<= acct:
	print('The root is:',b)
else:
	root = b(a,b,acct)
	print('The root is: ',root)