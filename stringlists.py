#String Lists
'''
Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.)
'''


text = str(input("Please enter a word: "))

rev = text[::-1]
print(rev)

if text == rev:
    print(text, " is a palindrome!")
else:
    print(text, " is not a palindrome!")
