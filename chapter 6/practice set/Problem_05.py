words = ["apple", "banana", "mango", "grapes"]

search = input("Enter string to find: ").lower()

if (search in words):
    print("String found")
    print("Index:" ,words.index(search))
else:
    print("String not found")
    