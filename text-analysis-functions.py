def count_words(text):
    words=text.split()
    return len(words)

def count_vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for ch in text:
        if ch in vowels:
            count=count+1
    return count

def count_consonants(text):
    vowels="aeiouAEIOU"
    count=0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count=count+1
    return count

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    text=text.lower()
    reverse_text==reverse_text(text)
    if text==reverse_text:
        return True
    else:
        return False
    
def remove_vowels(text):
    vowels="aeiouAEIOU"
    result=""
    for ch in text:
        if ch not in vowels:
            result=result+ch
    return result
        
def word_frequency(text):
    text=text.lower()
    words=text.split()
    freq={}
    for letter in words:
        if letter in freq:
            freq[letter]=1+freq
        else:
            freq[letter]=1
    return freq

def longest_word(text):
    words=text.split()
    if len(words)==0:
        return " "
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
                longest=word
        return longest

def analyze_text(text):
    print("------Text Analysis------")
    print("Number of words in text:",count_words(text))
    print("Number of vowels in text:",count_vowels(text))
    print("Number of consonants in text:",count_consonants(text))
    print("Reversed text :",reverse_text(text))
    print("If text is PALINDROME :",is_palindrome(text))
    print("Text where vowels are removed:",remove_vowels(text))
    print("The frequensy of words:",word_frequency(text))
    print("Longest word in the text:",longest_word(text))

text=input("Enter the text:")
analyze_text(text)



        