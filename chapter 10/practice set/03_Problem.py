class MyClass:
    a = 100

object = MyClass()
print(object.a) # prints class attributes ,  because instance attribute did not set
object.a = 0
print(object.a) # because it priors instance attributes 
print(MyClass.a) # Class attribute does not change , but an instance attribute sets