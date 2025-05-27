import math
def analyze_string(s):
    vowels = "aeiouAEIOU"
    vowel_chars = ''
    consonant_chars = ''
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_chars += char
            else:
                consonant_chars += char
                
    return (vowel_chars, len(vowel_chars), consonant_chars)
a = input("Enter a string: ")
result = analyze_string(str(a))
print(result)



