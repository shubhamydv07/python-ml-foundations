s1 = {1, 45, 6}

s2 = {7, 18, 1, 78}

s3 = {7 , 1 , 45 , 17}


print(s1.union(s2))  # give union

print(s1.intersection(s2)) # give intersection

print(s1.difference(s2))  # give s1 - s2

# GIVE UNION OF 3 SETS
print(s1.union(s2,s3))
print(s1.union(s2).union(s3))

# GIVE INTERSECTION OF 3 SETS
print(s1.intersection(s2,s3))
print(s1.intersection(s2).intersection(s3))

# GIVE DIFFERENCE OF 3 SETS NOTE :- IN DIFFERNECE ORDER MATTERS
print(s1.difference(s2,s3))
print(s1.difference(s2).difference(s3))

# GIVE SYMMETRIC DIFFERENCE OF 3 SETS , NOTE:-  MEANS REMOVES COMMON ELEMENT
print(s1.symmetric_difference(s2).symmetric_difference(s3))
print(s1^s2^s3)


# SOME LOGIC BASED OPERATIONS
print(s1.issubset(s2))  # SUBSET
print(s1.issuperset(s2))  # SUPERSET
print(s1.isdisjoint(s2))  #DISJOINT
