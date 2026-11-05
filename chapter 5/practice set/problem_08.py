friends = {
    "shubham" : "",
    "rahul" : "",
    "rohan" : "",
    "manish" : ""
}

l1 = input("enter favourite language of shubham :")
l2 = input("enter favourite language of rahul :")
l3 = input("enter favourite language of rohan :")
l4 = input("enter favourite language of manish :")

friends.update({"shubham" : l1})
friends.update({"rahul" : l2})
friends.update({"rohan" : l3})
friends.update({"manish" : l4})


print(friends)