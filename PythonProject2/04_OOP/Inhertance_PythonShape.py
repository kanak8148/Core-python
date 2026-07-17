class Shape:

    count =0


    def_init_(self,c,b):
    self.color = count
    self.boderWidth =b
    Shape.count += 1

    def __del__(self):
        className = self.__class__.__name__
        print("Destroying ", className)

    def area(self):
        print("i dont konw how to calculate area")
        return -1

    def info(self):
        print("Color: %s" % self.color)
        print("Border Width: %s" % self.borderWidth)

        def displayCount(self):
            print("Total Shape %d", Shape.count)

            def __str__(self):
                return "Circle: Color %s Border Width %i" % (self.color, self.borderWidth)

class Circle(Shape):
    PI = 3.14

    def_init_(self, r, c='',b=0):
    self.radius = r
    self.color = c
    self.boderWidth = b

    def area(self):
        return self.radius*self.radius * Circle.PI

    class Triangle(Shape):
        def_init_(self,base.height , c='',b=0):
        self.base =base
        self.height=height

