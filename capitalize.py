#Capitalize Words
def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    capitalized_sentence = ' '.join(capitalized_words)
    return capitalized_sentence

input_string = input("Enter a string to capitalize")
result = capitalize_words(input_string)
print(result)