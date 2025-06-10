import math
def analyze_string(s):
    vowels = "aeiouAEIOU"
    vowel_chars = ''
    consonant_chars = ''
    
    for d in s:
        if d.isalpha():
            if d in vowels:
                vowel_chars += d
            else:
                consonant_chars += d
                
    return (vowel_chars, len(vowel_chars), consonant_chars)
a = input("Enter a string: ")
result = analyze_string(str(a))
print(result)



