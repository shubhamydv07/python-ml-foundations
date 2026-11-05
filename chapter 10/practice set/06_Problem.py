from random import randint

class Train:

    def __init__(slf , trainNo):
        slf.trainNo = trainNo

    def book(shubham , fro , to):
        print(f"Ticket is booked in train no : {shubham.trainNo} from {fro} to {to}")

    def getstatus(slf):
        print(f"train no : {slf.trainNo} is running on time")

    def fare_info(slf , fro , to):
        print(f"Ticket fare in train no : {slf.trainNo} from {fro} to {to} is {randint(222 , 5555)}")

t = Train(14937)
t.book("kurukshetra" , "Delhi")
t.getstatus()
t.fare_info("kurukshetra" , "Delhi")