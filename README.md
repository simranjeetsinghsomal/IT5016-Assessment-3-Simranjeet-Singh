
# Typing Test Program

This program measures a user's typing speed and accuracy by asking them to type a given sentence. It calculates the correct characters per minute (cpm), words per minute (wpm), and accuracy percentage.

# How it works
The program sets a sentence for the user to type: "Programming is good but for coders".

It records the start time using the time module.

The user is prompted to type the sentence, and their input is recorded.

The program records the end time using the time module.

It calculates the total number of characters in the original sentence and the user's input.

The program compares the characters of both strings, incrementing a counter for each correct character.

It calculates the correct characters per minute (cpm), words per minute (wpm), and accuracy percentage using the following formulas:

cpm = correct characters / total time * 60
wpm = cpm / 5

accuracy = (correct characters / total characters) * 100

The program prints the calculated values: cpm, accuracy, wpm, and the total time taken.

# Code Structure

The program consists of a single function, Typing_Test, which contains the logic for the typing test.

# Variables and Functions

The function is called at the end of the script to run the program.

sen: the sentence to be typed by the user

start and end: the start and end times of the typing test, respectively

given_sen: the user's input sentence
total_characters and total_correct_characters: 

the total number of characters in the original sentence and the user's input, respectively

correct_characters: the number of correct characters typed by the user

cpm, wpm, and acc: the calculated correct characters per minute, words per minute, and accuracy percentage, respectively

Typing_Test: the main function that runs the typing test




## Deployment

To deploy this project run

```bash
  npm run deploy
```

