# THIS FUNCTION len() RETURNS THE VALUE OF LENGTH OF STRING
name = "shubham yadav"

print (len(name))

# VARIABLE STRING ENDS WITH SPECIFIC LETTER "string.endswith("ADAV")"
print (name.endswith("adav"))

# LIKE ENDS WITH IT ALSO HAVE STARTS WITH "string.startswith("SHUB")"
print(name.startswith("shub"))

# TO MAKE ALL CASES LOWER OR UPPER JUST WRITE .LOWER/.UPPER
print(name.lower())
print(name.upper())

# TO CAPITALIZE THE FIRST LETTER OF STRING USE .capitalize
print(name.capitalize())

# TO CAPITALIZE FIRST CHARACTER OF EACH WORD IN STRING USE .title()
print(name.title())

# count the total number of occurences of any character .count("letter")
print(name.count("h"))

#find any word and return index value .find(word)
print(name.find("y"))

# REPLACE TWO WORDS .replace(old word , new word)
print(name.replace("yadav" , "rao"))