def palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

text = input("Enter any text: ")

print(palindrome(text))