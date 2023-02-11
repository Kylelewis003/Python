import datetime

class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',date1= 0,date2= 0,rno=101,feedback = ' '):

        print ("\n\n*****WELCOME TO MARRIOT HOTELS*****\n")

        print ("Kindly fill Out Data In Given Order:- \nCustomer Data --> Room Rent --> Restaurant Bill(Optional) --> Laundry Bill(Optional) --> Game Bill(Optional) \n(Customer Details are necessary in order to generate Invoice)")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.date1=date1
        self.date2=date2
        self.rno=rno
        self.feedback = feedback
        chinmonth = 0
        chinyear = 0
        chindate = 0
        choutmonth = 0
        choutyear = 0
        choutday = 0

    def date(self):
       
        chinday = int(input("\nPlease enter the day for checkin date : "))
        chinmonth = int(input("\nPlease enter the month for checkin date : "))
        chinyear = int(input("\nPlease enter the year for checkin date  : "))
        choutday = int(input("\nPlease enter the day for checkout date : "))
        choutmonth = int(input("\nPlease enter the month for checkout date : "))
        choutyear = int(input("\nPlease enter the year for checkout date : "))

        self.date1 = datetime.date(chinyear,chinmonth,chinday)
        self.date2 = datetime.date(choutyear,choutmonth,choutday)

        print("\nCheck-in date:",self.date1)
        print("\nCheck-out date:",self.date2)
        print()

       
       
    def inputdata(self):
        self.name=str(input("\nEnter your Name:"))
        self.address=str(input("\nEnter your Address:"))
        print("\nName:",self.name)
        print("\nAddress:",self.address)
        print()

    def selectrooms(self):
        print ("\nWe have the following rooms for you:-")

        print ("\n1.  Standard Single Bed---->Rs 3000 Per Night\-")

        print ("\n3.  Standard Double Bed---->Rs 4000 Per Night\-")

        print ("\n3.  Luxury Standard suite---->Rs 5000 Per Night\-")

        print ("\n4.  Luxury Plus Suite---->Rs 6000 Per Night\-\n\nAll prices are Incusive Taxes*")

       

       
        y = input("\nWould you like to see the amenities of the rooms?(yes/no): ")

        if y == ("yes"):
            print("\n         ****** HOTEL ROOMS INFO ******    ")
            print("")
            print("1. Standard Single Bed")
            print("---------------------------------------------------------------")
            print("Room amenities include: 1 Single Bed, Television, Telephone,")
            print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
            print("an attached washroom with hot/cold water.\nExtra charges for WiFi*\n")
            print("2. Standard Double Bed")
            print("---------------------------------------------------------------")
            print("Room amenities include: 1 Double Bed, Television, Telephone,")
            print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
            print("an attached washroom with hot/cold water + Window/Split AC.\nExtra charges for WiFi*\n")
            print("3. Luxury Standard suite")
            print("---------------------------------------------------------------")
            print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
            print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
            print("Side table, Balcony with an Accent table with 2 Chair and an")
            print("attached washroom with hot/cold water.\nFree WiFi available*\n")
            print("4. Luxury Plus Suite")
            print("---------------------------------------------------------------")
            print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
            print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
            print("1 Side table, Balcony with an Accent table with 2 Chair and an")
            print("attached washroom with hot/cold water + Window/Split AC.\nFree WiFi available*\n\n")
            print()

            print("Please choose the room you would like to stay in after reading the Hotel room info :")

            print ("\n1.  Standard Single Bed---->rs 3000 Per Night\-")

            print ("\n3.  Standard Double Bed---->rs 4000 Per Night\-")

            print ("\n3.  Luxury Standard suite---->rs 5000 Per Night\-")

            print ("\n4.  Luxury Plus Suite---->rs 6000 Per Night\-")

        while True:
            try:
                x=int(input("\n1--> Standard Single Bed\n2-->Standard Double Bed\n3-->Luxury Standard Suite\n4-->Luxury Plus Suite\n\nEnter Response:"))
                if x < 1 or x > 4:
                    raise ValueError
                break
            except ValueError:
                print("Please enter valid response")
       
        n=int(input("How many nights would you like to stay?:"))

       

        if(x==1):

            print ("You have selected: Standard Single Bed")

            self.s=6000*n

        elif (x==2):

            print ("You have selected: Standard Double Bed")

            self.s=5000*n

        elif (x==3):

            print ("You have selected: Luxury Standard suite")

            self.s=4000*n

        elif (x==4):
            print ("You have selected: Luxury Plus Suite")

            self.s=3000*n

       
       
        print("Your room no.:",self.rno,"\n")


        print ("Your room rent will be Rs",self.s,"\n")
       

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.Water----->Rs20")
        print("2.Tea----->Rs10")
        print("3.Breakfast combo--->Rs90")
        print("4.Lunch---->Rs110")
        print("5.Dinner--->Rs150")
        print("6.Exit")


        while (1):

            c=int(input("\nEnter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity :"))
                self.r=self.r+20*d

            elif (c==2):
                 d=int(input("Enter the quantity :"))
                 self.r=self.r+10*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d

            elif (c==6):
                break;
            else:
                print("Invalid option")

        print ("\nTotal food Cost=Rs",self.r,"\n")

    def laundrybill(self):
        print ("******LAUNDRY MENU*******")

        print("1.Shorts----->Rs3")
        print("2.Trousers----->Rs4")
        print("3.Shirt--->Rs5")
        print("4.Jeans---->Rs6")
        print("5.Exit")

        while (1):

            e=int(input(":"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f

            elif (e==5):
               
                break
               
            else:

                print ("Invalid option")


        print ("\nTotal Laundary Cost=Rs",self.t,"\n")

    def gamebill(self):
        print ("******RECREATION MENU*******")

        print("1.Table tennis----->Rs60")
        print("2.bowling----->Rs80")
        print("3.Carrom--->Rs40")
        print("4.Video games---->Rs90")
        print("5.Pool--->Rs50")
        print("6.Exit")
        print("Rates Are Hourly*")


        while (1):

           
            g=int(input("Enter your choice:"))


            if (g==1):
                h=int(input("No. of hours:"))
                self.p=self.p+60*h

            elif (g==2):
                h=int(input("No. of hours:"))
                self.p=self.p+80*h

            elif (g==3):
                h=int(input("No. of hours:"))
                self.p=self.p+70*h

            elif (g==4):
                h=int(input("No. of hours:"))
                self.p=self.p+90*h

            elif (g==5):
                h=int(input("No. of hours:"))
                self.p=self.p+50*h
            elif (g==6):
                break;

            else:

                print ("Invalid option")



        print ("\nTotal Game Bill=Rs",self.p,"\n")

    def display(self):
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.date1)
        print ("Check out date",self.date2)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)
        print ("Your laundary bill is:",self.t)
        print ("Your Game bill is:",self.p)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1


a=hotelfarecal()


while (1):
    print("1.Enter Customer Data")

    print("2.Enter Checkin and Checkout date ")

    print("3.Select Rooms")

    print("4.Calculate restaurant bill")

    print("5.Calculate laundry bill")

    print("6.Calculate game bill")

    print("7.Show total cost")

    print("8.EXIT")

    b=int(input("\nEnter your choice:"))
    if (b==1):
       
        a.inputdata()

    if (b==2):

        a.date()

    if (b==3):

        a.selectrooms()

    if (b==4):

        a.restaurentbill()

    if (b==5):
       
        a.laundrybill()

    if (b==6):

        a.gamebill()

    if (b==7):

        a.display()

    if (b==8):      
        print("Thank You, Have a Good Day!\n\n")

        print("Software Created By Kyle Lewis B-22")
        print("Did you like it?(yes/no)")
       
        j=input("Enter response:")
       
        if j == ('yes'):
           
            print("Thank you! :)")
            break;
                   
        elif j == ('no'):
            feedback = input("Enter the feedback you would like to give :\n")
            print("\nYour Feedback:",feedback)
            print("\nThanks for your feedback! We'll make sure to improve it!")
            break;

        elif j != ("no") or j!= ("yes") :
            print("Invalid Input")
            break;
