class Device:
    def turn_on(self):
        pass
class Tv(Device):
    def turn_on(self):
        return "Tv is now on"

class Fan(Device):
    def turn_on(self):
        return "fan is now on"
    
class Light(Device):
    def turn_on(self):
        return "light is now on"
    
#function that uses polymorphism
def activate_device(device):
    print(device.turn_on())
    
tv = Tv() 
fan = Fan()
light = Light()


activate_device(tv)
activate_device(fan)
activate_device(light)
