class Car:
    def __init__(self, color, model, year) :
        self.color = color
        self.model = model
        self.year = year
        
    def details(self):
        print (self.color)
        print(self.model)
        print(self.year)
car1 = Car("black","tesla",2023)
car1.details()
        
        