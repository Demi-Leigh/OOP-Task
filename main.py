class Shapes: # Defining my super class
    # initialising my attributes
    def __init__(self, name, side, type, size,):
        self.name = name
        self.side = side
        self.type = type
        self.size = size

    def area(self):
        print("My name is : " + self.name + "\n" +
              "I have  : " + self.side + " sides" + "\n" +
              "My type is : " + self.type + "\n" +
              "My size is : " + self.size)


obj_Shapes = Shapes("Shape", "4", "Coin", "25")
obj_Shapes.area()


# Finding the circumference of a square
# Defining the subclass
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

# defining the method
    def area(self):
        result = 3.14 * self.radius * self.radius
        print(result)


# Printing the result
obj_coin = Circle(5)
obj_coin.area()


# finding the area of a triangle
# defining the subclass
class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

# defining the method
    def area(self):
        area_triangle = 0.5 * (self.height * self.base)
        return area_triangle


# Printing the result
obj_pyramid = Triangle(5, 10)
print(obj_pyramid.area())


# finding the area of a rectangle
# defining the subclass
class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

# defining the method
    def area(self):
        result = self.length * self.width
        print(result)


# printing the result
obt_rectangle = Rectangle(10, 20)
obt_rectangle.area()


# Finding the area of a square
# Defining the subclass
class Square(Shapes):
    def __init__(self, side):
        self.side = side

# defining the method
    def area(self):
        result = self.side ** 2
        print(result)


# printing the result
obt_square = Square(2)
obt_square.area()









