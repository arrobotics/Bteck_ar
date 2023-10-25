# Python3 code to find Gravitational Force
def force(m1, m2, r):
	G = 6.673*(10**-11)
	F = (G*m1*m2)/(r**2)

	# Rounding to two digits after decimal
	return round(F, 2) 

# Driver Code 
m1 = 5000000
m2 = 900000
r = 30
print("The Gravitational Force is: ", force(m1, m2, r), "N")
