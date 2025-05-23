def triangle():
	areaTriangle = (0.5*base*height)
	print("The area of Triangle is ", areaTriangle, "\n")

def rectangle(w,h):
	area = w * h
	print("The area of Rectangle is ", str(area), "\n")

def square(s):
	area = side * side
	print("The area of Square is ", str(area), "\n")

def circle(r=5.0, p=3.1416):
	area = p * (r * r)
	print(f"The area of Circle is ", str(area), "\n")

print("Area of Triangle")
base = int(input("base: "))
height = int(input("height: "))
triangle()

print("Area of Rectangle")
width = int(input("width: "))
height = int(input("height: "))
rectangle(width, height)

print("Area of Square")
side = int(input("side: "))
square(side)

print("Area of Circle")
circle()