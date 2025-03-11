class Shape:
    def __init__(self, name):
        self.name = name
    
    def perimeter(self):
        raise NotImplementedError("peremeter")

    def area(self):
        raise NotImplementedError("Area")