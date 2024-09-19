class Vehical():
    def __init__(self):
        pass
        
    def start (self):
        print("Vehical started")
    def stop(self):
        print("Vehical stopped")
class Car(Vehical):
    def hork(self):
        print("honk! honk!")
        
        
my_car = Car()
my_car.start()
my_car.hork()
my_car.stop()