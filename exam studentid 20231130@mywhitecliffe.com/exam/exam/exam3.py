'''
author :simranjeet singh somal
diseription:requistion approval

'''


def requisitions_total_amount():
    items = []
    total_amount = 0
    while True:
        item_name = input("Enter item name (or 'finish' to quit): ")
        if item_name.lower() == 'finish':
            break
        item_price = float(input("Enter the price of an item: "))
        items.append((item_name, item_price))
        total_amount += item_price

    print("\nrequistions_total:")
    for item in items:
        print(f"{item[0]}: ${item[1]:.2f}")
    print(f"\nTotal Amount: ${total_amount:.2f}")
    if total_amount > 350:
        print("status:uapproved")
        print("approval reference number: FN19001")
    else: total_amount < 350
    print("status:approved")
    print("approval reference number: FN19001")
    
requisitions_total_amount()

 