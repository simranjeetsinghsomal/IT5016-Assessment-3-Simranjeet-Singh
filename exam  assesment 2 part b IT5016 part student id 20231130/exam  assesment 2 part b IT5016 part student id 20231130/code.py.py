'''
Exam 
Author: simrajeet
Whitecliffe College, AKL
'''
class Requisition:
    def __init__(self, date, request_id, staff_id, staff_name, total, status, approval_ref):
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

# Create requisition objects
requisition1 = Requisition("3/4/2024", 10001, "FN19", "John Paul", 450, "approved", "FN19001")
requisition2 = Requisition("5/4/2024", 10002, "FN20", "Tracy Brown", 1000, "pending", "not available")
requisition3 = Requisition("7/5/2024", 10003, "FN15", "Emma Wellington", 3500, "not approved", "not available")
requisition4 = Requisition("3/5/2024", 10004, "FN02", "catlin white", 490, "approved", "FN02004")
# Display requisitions
print("Requisition 1:")
requisition1.display_requisition()
requisition1.check_status()

print("Requisition 2:")
requisition2.display_requisition()
requisition2.check_status()

print("Requisition 3:")
requisition3.display_requisition()
requisition3.check_status()

print("Requisition 4:")
requisition4.display_requisition()
requisition4.check_status()

#statistics:
print("statistics")
print("Displaying the requistion statistics")
print("The total number of requistion submitted: 4")
print("The total number of approved requistions: 2")
print("The total number of pending requistions: 1")
print("The total number of not approved requistions: 1")