def centimeters(centimeter):
    meter = centimeter
    return meter

def display_bmi(weight , height):
    bmi = weight/(height/100)**2
    return bmi

weight = float(input("weight"))

height = float(input("height"))
print(display_bmi(weight,height))