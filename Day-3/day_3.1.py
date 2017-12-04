
num = 361527
horDist = 0
vertDist = 0

for i in range (0, 600):
	if (num < ((2*i)+1)**2):
		horDist = i
		vertDist = i-((((2*i)+1)**2-num)%i)
		break

#The -1 is because the distance is zero indexed
print(horDist+vertDist-1)
#I tried to do this one very quickly so I did the final calculation in my head...
#This solution is actually wrong for the general problem, but it worked for this one.
#I finished 331 in the world

