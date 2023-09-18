class Car :
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def introduce_self(self):
        print("Mobilku adalah " + self.name, ", Mobilku berwarna " + self.color)

c1 = Car('Civic','Merah')
c2 = Car('Brio','Kuning')
c3 = Car('Ayla', 'Silver')

c1.introduce_self()
c2.introduce_self()
c3.introduce_self()
