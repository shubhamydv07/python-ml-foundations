def main():

    try:
        a = int(input("enter any number"))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:  # if we will not use finally here then, below print will not run , otherwise it will run
        print("Heyy I am inside finally block")

main()