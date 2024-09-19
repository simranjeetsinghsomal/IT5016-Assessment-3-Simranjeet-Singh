class Requisition:
    def _init_(self, date, request_id, staff_id, staff_name, total, status, approval_ref):
        self.date = date
        self.request_id = request_id
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.total = total
        self.status = status
        self.approval_ref = approval_ref

    def display_requisition(self):
        print(f"Date: {self.date}")
        print(f"Request ID: {self.request_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_ref}")
        print()

    def check_status(self):
        if self.status == "approved":
            print("Requisition is approved.")
        elif self.status == "pending":
            print("Requisition is pending.")
        else:
            print("Requisition is not approved.")

    @classmethod
    def register(cls):
        date = input("Enter date: ")
        request_id = int(input("Enter request ID: "))
        staff_id = input("Enter staff ID: ")
        staff_name = input("Enter staff name: ")
        total = float(input("Enter total: "))
        status = input("Enter status (approved/pending/not approved): ")
        approval_ref = input("Enter approval reference number: ")
        return cls(date, request_id, staff_id, staff_name, total, status, approval_ref)

# Create requisition objects
requisitions = []

while True:
    print("1. Register a new requisition")
    print("2. Display all requisitions")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        requisition = Requisition.register()
        requisitions.append(requisition)
    elif choice == "2":
        for i, requisition in enumerate(requisitions, start=1):
            print(f"Requisition {i}:")
            requisition.display_requisition()
            requisition.check_status()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

# statistics:
print("statistics")
print("Displaying the requisition statistics")
print(f"The total number of requisitions submitted: {len(requisitions)}")
approved_count = sum(1 for requisition in requisitions if requisition.status == "approved")
pending_count = sum(1 for requisition in requisitions if requisition.status == "pending")
not_approved_count = sum(1 for requisition in requisitions if requisition.status == "not approved")
print(f"The total number of approved requisitions: {approved_count}")
print(f"The total number of pending requisitions: {pending_count}")
print(f"The total number of not approved requisitions: {not_approved_count}")