def area(w,h):
	area_rectangle = w * h

	perimeter_rectangle = 2 * (w + h)

        print("\n Area of a Rectangle is: %.2f" %area_rectangle)

        print(" Perimeter of Rectangle is: %.2f" %perimeter_rectangle)




width = float(input('Please Enter the Width of a Rectangle: '))
height = float(input('Please Enter the Height of a Rectangle: '))


rectangle = area(width,height)


