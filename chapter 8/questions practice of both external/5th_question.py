def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count = count + 1
    return count
        
s = input("Enter any string: ")
print(f"the number of vowels in {s} is {count_vowels(s)}")