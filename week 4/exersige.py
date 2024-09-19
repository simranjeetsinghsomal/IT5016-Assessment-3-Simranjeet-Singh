def shoopin_list():
    shooping_list=[]#it is a list that store values.
    total_price = 0
    while True:
        iteam = input("enter the name of the iteam(or type'done'to finish):")
        if iteam.lower()=='done':
            break
        try: 
            price = float(input(f"enter the price of '{iteam}':"))
            shooping_list.append((iteam,price))
            total_price+=price
        except ValueError:
            print("invalid input.please enter a numeric value for the price")
            
        return shooping_list,total_price


def main():
    print("welcome to shoping list program")
    shooping_list, total_price = shoopin_list()
    if not shoopin_list:
        print("no itmes were entered")
    else:
        print("/nshooping_list:")
        for item, price in shoopin_list:
            print(f"{item},${price:.2f}")
        print(f"/nTotal price:${total_price:.2f}")    
    
main()