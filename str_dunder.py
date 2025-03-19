class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"This is a rectangle with height {self.height} and width {self.width}"
    

r = Rectangle(5,10)
print(r)