f = open("poems.txt" , "r")

read = f.read()

if "twinkle" in read:
    print("Twinkle is present")
else:
    print("Twinkle is not present")

f.close()