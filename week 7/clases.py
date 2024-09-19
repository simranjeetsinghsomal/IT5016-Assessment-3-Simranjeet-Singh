class Person():
    #constructor
    def __init__(self, name,  gender):
        self.name = name
        self.age = 10
        self.gender = gender
        self.gender = gender
        
    def speaks(self ):
        quote = input(f"What does the {self.name} say ?:")
        print(quote)
        
    #object
person1 = Person("rashid","male")
person2 = Person("Kanchan","female")
person1.speaks()