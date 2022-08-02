class RailwayCounter:
    def __init__(self, name, tickets, seatType, from_place, to_destinaion):
        self.name = name
        self.tickets = tickets
        self.seatType = seatType
        self.from_place = from_place
        self.to_destination = to_destinaion

    def print_receipt(self):
        print("Name : ", self.name)
        print("No.of Tickets: ", self.tickets)
        print("Seat ype: ", self.seatType)
        print("From :", self.from_place, "        To: ", self.to_destination)


class Traveller(RailwayCounter):
    def __init__(self):
        self.name = input("Enter your name: ")
        self.from_place = input("Enter your Boarding Station:")
        self.to_destination = input("Enter to destination:")
        self.tickets = int(input("Enter no.of Tickets:"))
        self.seatType = input("Enter seat_Type:")
        RailwayCounter.__init__(self, self.name, self.tickets, self.seatType, self.from_place, self.to_destination)


rider = Traveller()
rider.print_receipt()

