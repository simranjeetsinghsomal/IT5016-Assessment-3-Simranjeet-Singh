from time import time

def Typing_Test():    

    sen = "Programming is good but for coders"
    print(">>", sen)

    start = time()
    given_sen = input(">> ")
    end = time()

    total_characters = len(sen)
    total_correct_characters = len(given_sen)
    j = min(total_characters, total_correct_characters)
    correct_characters = 0

    for i in range(j):
        if sen[i] == given_sen[i]:
            correct_characters += 1

    Total_time = round((end - start), 2)

    cpm = round(correct_characters/Total_time)*60
    wpm = round(cpm/5)
    acc = round((correct_characters/j)*100)  # Corrected accuracy calculation

    print("cpm", cpm)
    print("acc", acc)
    print("wpm", wpm)
    print("Your Time", Total_time)

Typing_Test()