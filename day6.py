#created by vijay pratap singh
#created date 18-01-2017
#to calculate area and perimeter of rectangle.


class rect:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y




rectangle = rect(10,20)


print'area of rectangle is:', rectangle.area()
print 'perimeter of rectangle is:',rectangle.perimeter()



 
