Vaibhav
Kashyap, [13.06.21 0o1: 0o6
]

class hotelmanagement:

    def init(self, rt='', s=0, p=0, r=0, t=0, a=700, name='', address='', cindate='', coutdate='', rno=101):

        print("\n\n*****HELLO COTTAGE*****\n")

        self.rt = rt

        self.r = r

        self.t = t

        self.p = p

        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.indate = cindate
        self.outdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your address:")
        self.cindate = input("\nEnter your check in date:")
        self.coutdate = input("\nEnter your checkout date:")
        print("Your room no.:", self.rno, "\n")

    def roomrent(self):

        print("We have the following rooms for you:-")

        print("1.  type A(AC-Dual bed)---->rs 3000 PN\-")

        print("2.  type B(AC-Single bed)---->rs 2000 PN\-")

        print("3.  type C(Non AC-Dual bed)---->rs 1500 PN\-")

        print("4.  type D(Non AC-Single bed)---->rs 900 PN\-")

        x = int(input("Enter Your Choice Please->"))

        n = int(input("For How Many Nights Did You Stay:"))

        if (x == 1):

            print("you have opted room type A")

            self.s = 3000 * n

        elif (x == 2):

            print("you have opted room type B")

            self.s = 2000 * n

        elif (x == 3):

            print("you have opted room type C")

            self.s = 1500 * n

        elif (x == 4):
            print("you have opted room type D")

            self.s = 900 * n

        else:

            print("please choose a room")

        print("your room rent is =", self.s, "\n")

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.water----->Rs20", "2.tea----->Rs10", "3.breakfast combo--->Rs90", "4.lunch---->Rs110",
              "5.dinner--->Rs150", "6.Exit")

        while (1):

            c = int(input("Enter your choice:"))

            if (c == 1):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 20 * d

            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 10 * d

            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 90 * d

            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 110 * d

            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 150 * d

            elif (c == 6):
                break
            else:
                print("Invalid option")

        print("Total food Cost=Rs", self.r, "\n")

    def laundrybill(self):
        print("******LAUNDRY MENU*******")

        print("1.Shorts----->Rs3", "2.Trousers----->Rs4", "3.Shirt--->Rs5", "4.Jeans---->Rs6", "5.Girlsuit--->Rs8",
              "6.Exit")

        while (1):

            e = int(input("Enter your choice:"))

            if (e == 1):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 3 * f

            elif (e == 2):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 4 * f

            elif (e == 3):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 5 * f

            elif (e == 4):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 6 * f

            elif (e == 5):
                f = int(input("Enter the quantity:"))
                self.t = self.t + 8 * f
            elif (e == 6):
                break
            else:

                print("Invalid option")

        print("Total Laundary Cost=Rs", self.t, "\n")


Vaibhav
Kashyap, [13.06.21 0o1: 0o6
]

def display(self):
    print("******HOTEL BILL******")
    print("Customer details:")
    print("Customer name:", self.name)
    print("Customer address:", self.address)
    print("Check in date:", self.cindate)
    print("Check out date", self.coutdate)
    print("Room no.", self.rno)
    print("Your Room rent is:", self.s)
    print("Your Food bill is:", self.r)
    print("Your laundry bill is:", self.t)

    self.rt = self.s + self.t + self.p + self.r

    print("Your sub total bill is:", self.rt)
    print("Additional Service Charges is", self.a)
    print("Your grandtotal bill is:", self.rt + self.a, "\n")
    self.rno += 1


def main():
    a = hotelmanagement()

    while (1):
        print("1.Enter Customer Data")

        print("2.Calculate roomrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Show total cost")

        print("6.EXIT")

        b = int(input("\nEnter your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.roomrent()

        if (b == 3):
            a.restaurentbill()

        if (b == 4):
            a.laundrybill()

        if (b == 5):
            a.display()

        if (b == 6):
            quit()


main()
