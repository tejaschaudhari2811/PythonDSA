class Sample:
    n_objects = 0

    def __init__(self, name):
        self.name = name
        Sample.n_objects +=1

    def how_many_objects(self):
        print("There are", Sample.n_objects)

    def __del__(self):
        Sample.n_objects -=1

    
oSample1 = Sample('A')
oSample2 = Sample('b')
oSample3 = Sample('bA')
oSample4 = Sample('d')

print(oSample1.how_many_objects())

del oSample3

print(oSample1.how_many_objects())
