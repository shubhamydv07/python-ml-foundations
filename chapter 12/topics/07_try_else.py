try:
    a = int(input("enter any number"))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")


# If we use try else together , then If try runs succesfully ,then it will automatically
# move to the else block , otherwise not run else block