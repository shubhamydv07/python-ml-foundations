def rem(l , word):
        t = []
        for item in l:
            if not(item==word):
                  t.append(item.strip(word))
        return t          

l = ["shubham" , "rohan" , "harry" , "simran" , "an"]

word = input("enter the word you want to remove :")

print(rem(l , word))
