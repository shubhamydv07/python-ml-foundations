class twoDvector:
    def __init__(self , i , j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j")

    
class threeDvector(twoDvector):
    def __init__(self , i , j , k):
        super().__init__(i , j)
        self.k = k

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

a = twoDvector(1 , 2)
b = threeDvector(5 , 8 , 3)

a.show()
b.show()
