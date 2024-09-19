def what_to_do_now():
    messge = "time to"
    prompt = "enter seond (1,2or3):"
    user_choice = int(input(prompt))
    
    if user_choice == 1:
        print(messge,"eat")
    elif user_choice==2:
        print(messge,"play")
    elif user_choice == 3:
        print(messge,"sleep")
    else:
        print("incorrect selection!")

what_to_do_now()