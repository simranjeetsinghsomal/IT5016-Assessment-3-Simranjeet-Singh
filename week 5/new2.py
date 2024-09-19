def calculate_total_amount():
    items = []
    total_amount = 0
    while True:
        item_name = input("Enter item name (or 'finish' to quit): ")
        if item_name.lower() == 'finish':
            break
        item_price = float(input("Enter the price of an item: "))
        items.append((item_name, item_price))
        total_amount += item_price

    print("\nShopping List:")
    for item in items:
        print(f"{item[0]}: ${item[1]:.2f}")
    print(f"\nTotal Amount: ${total_amount:.2f}")
    
calculate_total_amount()

 