class Attendee:

    def __init__(self,name,tickets):
        self.name=name
        self.tickets=tickets

    def dispalyAttendee(self):
        print("Name : {}, Tickets : {}".format(self.name,self.tickets))

    def addTickets(self):
        self.tickets+=1
        print("{} tickets increased to {}".format(self.name,self.tickets))

attendee1 = Attendee("Bac",2)
attendee2=Attendee("Jaq",4)
attendee1.dispalyAttendee()
attendee2.addTickets()
attendee2.addTickets()
attendee2.dispalyAttendee()