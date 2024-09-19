'''
author :simranjeet singh somal
diseription:create staff id
'''
def staff_info(id):
    print("enter staff information")
    date = input("date:")
    staff_id = input("staffid")
    satfff_name = input("staffname")

    unique_id = id + 1
    id = unique_id

    print("staff employee information")
    print("user name:",satfff_name)
    print("user id", staff_id)
    print("user date", date)
    print("requisition id",unique_id)


def main():
        id = 10000
        staff_info(id)
main()
