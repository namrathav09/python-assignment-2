sentence=input("Enter a string:")

print("1.The ORIGINAL string is :",sentence)

length_with_space=len(sentence)
print("2.The total characters WITH SPACES:",length_with_space)

length_without_space=len((sentence.replace(" ","")))
print("3.The total characters WITHOUT SPACES:",length_without_space)

word=sentence.split(" ")
word_count=len(word)
print("4.The total WORDS in sentence:",word_count)

upper_case=sentence.upper()
print("5.The sentence in UPPERCASE:",upper_case)

lower_case=sentence.lower()
print("6.The sentence in LOWERCASE:",lower_case)

title_case=sentence.title()
print("7.The sentence in TITLECASE:",title_case)

first_word=word[0]
print("8.The first word in the sentence:",first_word)

last_word=word[-1]
print("9.The first word in the sentence:",last_word)

reversed_string=sentence[::-1]
print("10.The reversed sentence :",reversed_string)

