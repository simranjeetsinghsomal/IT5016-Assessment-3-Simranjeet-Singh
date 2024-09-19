name = input("enter your name")
age = input("enter you age")
print("hello",name,".you are", age , "year old",sep="")
#fstring

print(f"hello,{name}.you are {age}years old.")
pi = 3.1415926589
formatted_pi = f"value of pi to 2 decimal place:{pi:.2f}"
print(formatted_pi)

salar = float(input("enter your weekly salary:"))
print(f"your weekly salary is ${salar:.2f}")

a = 10 
b = 5 
result = f"the result of {a} multiplied by {b} is {a*b}"
print(result)

name ="jeams"
age = 28
address ="121 queen st"
info = f"""
name:{name}
age:{age}
address:{address}
"""
print(info)