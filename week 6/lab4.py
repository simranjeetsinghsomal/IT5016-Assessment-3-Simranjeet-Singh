class Car():
    def  __init__(self,brand,model,year,color):
        self.brand = brand
        self.model = model
        self.year  = year
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.brand} {self.model} has stopped.")

    def info(self):
        print(f" Car Info: {self.year} {self.color} {self.brand}  {self.model}")

car1=Car("Ford","Mustang",2023,"Blue")


car1.drive()
car1.stop()
car1.info()