#Welcome user
print("Welcome to Palindrome")

#Tell user to input a string
word = input("Enter A Word: ")

#remove white spaces
word = word.replace(" ", "")

#display string
print("You inputed: "+ word)

# Reverse the string
def reversed_string(val):
    return val[::-1]

backword = reversed_string(word)

if word == backword:
    print(word+" IS a Palindrome")
else:
    print(word + " is NOT a Palindrome")