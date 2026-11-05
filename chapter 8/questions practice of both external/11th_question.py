def caesar(text, shift):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

text = input("Enter the text you want to encrypt: ")
shift = int(input("Enter the shift number: "))

if shift < 0:
    print("Error! Please enter a positive shift.")
else:
    print(f"The encrypted text is: {caesar(text, shift)}")