class Person:
    def __init__(self):
        self.A ="james"
        self._B ="james bound"
    def PrintName(self):
        print(self.A)
        print(self._B)
        
p = Person()
p.A
p._B 
        