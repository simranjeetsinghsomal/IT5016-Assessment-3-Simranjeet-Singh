class RequestSystem():
    counter_id = 1000

    def __init__(self):  # Fix: _init_ -> __init__
        self.id = RequestSystem.counter_id
        RequestSystem.counter_id += 1
        self.name = None
        self.age = None
        self.email = None
        self.total = 0

    def register(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.email = input("Enter your email: ")
        return f"Registered successfully! Your ID is {self.id}"

    def request_details(self):
        items = []
        prices = []
        total = 0
        while True:
            item = input("Enter item name: ")
            if item == "done":
                break
            price = input("Enter item price: ")
            items.append(item)
            prices.append(int(price))  # convert price to int
            total += int(price)  # add to total
        self.total = total  # store the total in the object
        return total

    def request_approval(self):
        if self.total > 150:
            return "Request approved"
        else:
            return "Request denied"

    def respond_request(self):
        if self.total < 150:
            return "Not approved"
        else:
            return "Approved"

    def display_request(self):
        print("Displaying all Information")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Total: {self.total}")

def main():
    request_system = RequestSystem()
    while True:
        print("1. Register")
        print("2. Request details")
        print("3. Display all information")
        print("4. Request approval")
        print("5. Respond to request")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(request_system.register())
        elif choice == "2":
            request_system.request_details()
        elif choice == "3":
            request_system.display_request()
        elif choice == "4":
            print(request_system.request_approval())
        elif choice == "5":
            print(request_system.respond_request())
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":  # Fix: "_main_" -> "__main__"
    main()