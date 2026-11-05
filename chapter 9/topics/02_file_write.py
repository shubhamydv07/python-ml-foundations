# whenever we open file in write mode using "w" , it erase file complete and then it opens in write mode

st = ("Hey shubham , how are you , I am rohit ")

f = open("myfiles.txt" , "w") # opens in write mode

f.write(st) # it will write st in f
f.close()  # close f