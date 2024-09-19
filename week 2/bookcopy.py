"""
calculate the whole sale of cost for 60 copies
 Author: simran
 """
#input
book_cover_price = 24.95
discount = 40/100
copies = 60

#process
book_discount_price = book_cover_price*discount
#book price after discount
unit_price = book_cover_price - book_discount_price

total = unit_price*copies

shipping = 3 + 0.75*(copies - 1)

grand_total = total + shipping
print(grand_total)
#output