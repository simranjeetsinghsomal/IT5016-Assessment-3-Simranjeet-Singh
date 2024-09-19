#"""wavelength author simran"""
#def wavelength():
    #nm = int(input("enter the nm"))
    #if 620>nm<750:
        #print("red")
    #elif 590>nm<620:
        #print("orange")
    #elif 570>nm<590:
        #print("yellow")
    #elif 495>nm<570:
        #print("green")
    #elif 450>nm<495:
        #print("blue")
    #elif 380>nm<450:
        #print("violet")
    #else:
        #print("error")
#wavelength()



def magnitude_detector():
    magnitude = float(input("Please enter magnitude of the earthquake:" ))
    if magnitude < 2.0:
        print("Micro")
    elif magnitude >= 2.0 and magnitude < 3.0:
        print("Very Minor")
    elif magnitude >= 3.0 and magnitude < 4.0:
        print("Minor")
    elif magnitude >= 4.0 and magnitude < 5.0:
        print("light")
    elif magnitude >= 5.0 and magnitude < 6.0:
        print("Moderate")
    elif magnitude >= 6.0 and magnitude < 7.0:
        print("Strong")
    elif magnitude >= 7.0 and magnitude < 8.0:
        print("Major")
    elif magnitude >= 8.0 and magnitude < 10.0:
        print("great")
    else:
        print("meteoric")


def main():
   magnitude_detector()
main()