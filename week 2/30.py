#iteam1 = 100
#iteam2= 15
#iteam3 = 20

iteam1 = float(input("Enter the price for iteam1:"))
iteam2= float(input("Enter the price for iteam2:"))
iteam3 = float(input("Enter the price for iteam3:"))


subTotal = iteam1 + iteam2 + iteam3
salesGST = subTotal * 0.15
total = subTotal + salesGST
print("your purchase total is $", total,sep="")