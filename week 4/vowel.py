def count_vowels(text):
    vowels = " aeiou"
    count = 0
    for char in text:
        if char.lower()in vowels:
         count +=1
    return count 
def mian():
    text = input("enter the text:")
    vowel_count= count_vowels(text)
    print(f"number of vowels in {text}:{vowel_count}")

mian()
