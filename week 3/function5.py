def function3(word):
    first = word[0]
    last =word [len(word)-1]
    combined = last + first
    return combined.upper()
word = input ("enter a word>>")
print (function3(word))