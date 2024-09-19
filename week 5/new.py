'''
Authot:simran
Creat user id

'''

def collect_user_data(id_counter):
   
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    unique_id = id_counter + 1
   
    print(f"\nUser Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Unique ID: {unique_id}")
   
    return unique_id
 
def main():
    id_counter = 5000
    new_id = collect_user_data(id_counter)
   
    id_counter = new_id
    print(f"\nUpdated ID Counter: {id_counter}")
 
if __name__ == "__main__":
    main()