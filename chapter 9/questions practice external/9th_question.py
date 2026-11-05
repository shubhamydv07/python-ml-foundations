with open("hello.txt" , "r") as f:
    content = f.readlines()

for i in range (len(content)):
    print(f"{i+1}.{content[i]}")

    
while True:
    try:
        position = int(input("enter the line you want to remove:"))
        if position < 1 or position > len(content):
            raise ValueError
        break
    except ValueError:
        print(f"enter number from 1 to {len(content)}")

updated = content.pop(position-1)

with open("hello.txt" , "w") as f:
    f.writelines(content)

