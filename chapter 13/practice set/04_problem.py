numbers = [12 , 45,56,78,30,15,10,24,68]

def five_divisible(n):
    if n%5 == 0:
        return True
    return False

new_list = filter(five_divisible , numbers)
print(list(new_list))
        
