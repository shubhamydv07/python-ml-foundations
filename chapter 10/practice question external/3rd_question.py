class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        if self.count > 0:
            self.count -= 1
        else:
            print("Count is already at 0!")

    def reset(self):
        self.count = 0

    def get_count(self):
        return self.count


counter = Counter()

print("Starting from zero")

while True:
    print("Current count:", counter.get_count())
    print("1. Increment")
    print("2. Decrement")
    print("3. Reset")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        counter.increment()
    elif choice == "2":
        counter.decrement()
    elif choice == "3":
        counter.reset()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting the program.")