import math

radius_str = input("Enter of the radius of circle:")
radius_int = int(radius_str)
circumference = 2 * math.pi * radius_int
area = math.pi * (radius_int **2 )

print ("The cicumference is:",circumference, \
	", and the area is: ",area)