text= input("Enter word/Number:")

original=text
lower_text =text.lower()
reversed_text=lower_text[::-1]

print("Original:" ,original)
print("Reversed:",reversed_text)
if lower_text == reversed_text:
    print("Result:PALINDROME")
else:
    print("Result:hell yea its not a palindrone")

#palindrome is something which repeats itself when its made reverse