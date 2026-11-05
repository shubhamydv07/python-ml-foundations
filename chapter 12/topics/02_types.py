from typing import List, Tuple, Dict, Union

n : int = 54

name : str = "Shubham Yadav"

# if i use n. or name. , then it will show me all types of methods after use the int, str etc.


def sum(a : int , b : int)  ->int:  # "-> str" this will tell the type of return in function
    return a+b

result = sum(25,35)

print(f"The sum is: {result}")
print(sum.__annotations__)


# List of integers 
numbers:List[int] = [1, 2, 3, 4, 5] 

# Tuple of a string and an integer 
person: Tuple[str, int] = ("Alice", 30) 

# Dictionary with string keys and integer values 
scores: Dict[str, int] = {"Alice": 90, "Bob": 85} 

# Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid

# These annotations help in making the code self-documenting 
# and allow developers to understand the data structures used at a glance.