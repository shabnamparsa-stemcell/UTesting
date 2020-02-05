# Python Program to find Area Of Circle using Radius

# PI = 3.14
# radius = float(input(' Please Enter the radius of a circle: '))
# area = PI * radius * radius
# circumference = 2 * PI * radius

# print(" Area Of a Circle = %.2f" %area)
# print(" Circumference Of a Circle = %.2f" %circumference)

from math import pi


def circle_area(r):
    return pi * (r ** 2)

# test function
# radii = [2,0,0,0,True,"radius"]
# message = "Area of circles with r= {radious} is {area}."

# for r in radii:
#    A = circle_area(r)
#   print(message.format(radious=r, area=A))
