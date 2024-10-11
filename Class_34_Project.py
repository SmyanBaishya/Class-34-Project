import math

#Defining the class Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius #Constructor that initializes the radius
    
    #Method to calculate the area
    def area(self):
        return math.pi * self.radius ** 2

    #Method to calculate the perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius

#Get input from the user
radius = float(input("Enter the radius of the circle: "))

#Create an instance of the Circle class
circle = Circle(radius)

#Calculate and display the area and perimeter
print("Area of the circle: ", circle.area())
print("Perimeter of the circle: ", circle.perimeter())
    


