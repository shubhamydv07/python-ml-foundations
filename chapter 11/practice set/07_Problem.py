class Vector:
    def __init__(self , list):
        self.l = list
    
    def __len__(self):
        return len(self.l)
    

a = Vector([2 , 4 , -6])

print(len(a))