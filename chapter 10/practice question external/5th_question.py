class Circle:

    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return (3.14159 * self.radius * self.radius)
        
    def circumference(self):
        return (2 * 3.14159 * self.radius)

circle = Circle(10)
print(circle.area())
print(circle.circumference())

