def function1(n1,n2,n3):
    sum = n1 + n2+ n3 
    minimun = min(n1, n2, n3)
    return sum - minimun

    n1 = int(input("number 1:"))
    n2 = int(input("number 2:"))
    n3 = int(input("number 3:"))
    print(function1 (n1,n2,n3))

