def total_user_number():
    total = 0
    number = int(input("enter a number(0 to end):"))
    while number !=0:
        total += number
        number=int(input("enter  NUMBER (0 to end):"))
    print("Total:",total)
        
    
def main():
    total_user_number()
main()