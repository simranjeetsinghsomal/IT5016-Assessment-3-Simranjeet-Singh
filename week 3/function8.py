def get_price (child,adult):
    child_price = 10
    adult_price = 25
    group_size = 14
    group_rate = 0.9
    
    cost = (child * child_price + adult* adult_price)
    
    if child + adult > group_size:
       cost  = cost * group_rate
    return cost 
def main():
    num_child = int (input("enter the umber of children:"))
    num_adult = int (input("enter the umber of adults:"))
    cost = get_price(num_child,num_adult)
    print("the cost of your ticket is : $ "+ str(cost))
main()