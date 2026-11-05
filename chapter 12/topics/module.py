def MyFunc():
    print("Hello World!")



if __name__ == "__main__":
    print("We are directly running this code")

    MyFunc()
    print(__name__) # output - __main__ , because we run it from main file

elif __name__ == "module":
    print("We are importing this code")
    MyFunc()
    print(__name__)