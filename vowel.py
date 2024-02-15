#count vowels

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

sentence = input("Enter a sentence: ")
num_vowels = count_vowels(sentence)
print("Number of vowels:", num_vowels)