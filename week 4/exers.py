def reverse_string(s):
    reversed_str =""
    for char in s :
        reversed_str = char + reversed_str
    return reversed_str
    
    
    
def main():
    original_string = input("enter a string:")
    reverse_string= original_string[::-1]
    print(f"original:{original_string}")
    print(f"reversed:{reverse_string}")
main()
