#Flight Management System
#Using Python and MySQL

#Connecting with MySQL
import mysql.connector as C
mycon = C.MySQLConnection(host = "localhost", user = "root", passwd = "mudit@MySQL", database = "FMS")
cursor = mycon.cursor()

#Creating Tables in a database FMS
cursor.execute("CREATE TABLE IF NOT EXISTS Passengers( BookingID integer, Head varchar(30), NumOfPass integer, FlightNum integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS Flights ( FlightNum integer, Date varchar(30), TOA varchar(10), Dest varchar(30), TOD varchar(10))")

#Operating the Passengers' Database
def Pass():
    
    print("What do you wish to do?")
    print("1. Add a passenger")
    print("2. Remove a passenger")
    print("3. Get the details of a passenger")
    print("4. Update the details of a passenger")
    print("5. Display total number of passengers per flight")
    print("6. Display destinations of each passenger")
    print("7. Display the database")
    c = int(input("Enter choice: "))
    
    if c == 1:
        BID = int(input("Booking ID: "))
        Name = input("Name of Passenger: ")
        NP = int(input("Number of Passengers: "))
        FN = int(input("Flight Number: "))
        sql = "INSERT INTO Passengers VALUES ({},'{}',{},{})".format(BID,Name,NP,FN)
        try:
            cursor.execute(sql)
            mycon.commit()
            print("Passenger added successfully")
        except:
            print("Incompatible values entered!")
            
    elif c == 2:
        BID =int(input("Enter the Booking ID of the passenger to be removed: "))
        sql = "DELETE FROM Passengers WHERE BookingID = {}".format(BID)
        try:
            cursor.execute(sql)
            mycon.commit()
            print("Passenger removed successfully!")
        except:
            print("Booking ID NOT FOUND")
            
    elif c == 3:
        BID =int(input("Enter the Booking ID of the passenger to be checked: "))
        sql = "SELECT * FROM Passengers WHERE BookingID = {}".format(BID)
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            print("Displaying passenger details")
            for row in data:
                print(row)
        except:
            print("Booking ID NOT FOUND")
            
    elif c == 4:
        BID =int(input("Enter the Booking ID of the passenger to be updated: "))
        sql = "DELETE FROM Passengers WHERE BookingID = {}".format(BID)
        try:
            cursor.execute(sql)
            mycon.commit()
            print("Passenger removed successfully!")
        except:
            print("Booking ID NOT FOUND")
        Name = input("Name of Passenger: ")
        NP = int(input("Number of Passengers: "))
        FN = int(input("Flight Number: "))
        sql = "INSERT INTO Passengers VALUES ({},'{}',{},{})".format(BID,Name,NP,FN)
        try:
            cursor.execute(sql)
            mycon.commit()
            print("Passenger added successfully")
        except:
            print("Incompatible values entered!")

    elif c == 5:
        cursor.execute("SELECT FlightNum, SUM(NumOfPass) FROM Passengers GROUP BY FlightNum")
        data = cursor.fetchall()
        print("Displaying the details")
        for row in data:
            print(row)

    elif c == 6:
        cursor.execute("SELECT Passengers.FlightNum, BookingID, Head, Flights.Dest FROM Passengers, Flights WHERE Passengers.FlightNum = Flights.FlightNum")
        data = cursor.fetchall()
        print("Displaying the details")
        for row in data:
            print(row)

    elif c == 7:
        cursor.execute("SELECT * FROM Passengers")
        data = cursor.fetchall()
        print("Displaying the databse")
        for row in data:
            print(row)

    else:
        print("Please enter a valid choice")

#Operating the Flights Database
def Flig():
    
    print("What do you wish to do?")
    print("1. Add a Flight")
    print("2. Remove a Flight")
    print("3. Get the details of a Flight")
    print("4. Update the details of a Flight")
    print("5. Display the Whole Database")
    c = int(input("Enter choice: "))

    if c == 1:
        FN = int(input("Flight Number: "))
        D = input("Date of flight: ")
        TA = input("Time of Arrival: ")
        Des = input("The Destination: ")
        TD = input("Time of Departure: ")
        sql = "INSERT INTO Flights VALUES ({},'{}','{}','{}','{}')".format(FN,D,TA,Des,TD)
        try:
            cursor.execute(sql)
            mycon.commit()
            print("Flight added successfully")
        except:
            print("Incompatible values entered!")

    elif c == 2:
        FN =int(input("Enter the Flight Number of the Flight to be removed: "))
        sql = "DELETE FROM Flights WHERE FlightNum = {}".format(FN)
        try:
            cursor.execute(sql)
            mycon.commit()
            print("Flight removed successfully!")
        except:
            print("Flight NOT FOUND")

    elif c == 3:
        FN =int(input("Enter the Flight Number of the Flight to be checked: "))
        sql = "SELECT * FROM Flights WHERE FlightNum = {}".format(FN)
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            print("Displaying Flight details")
            for row in data:
                print(row)
        except:
            print("Flight NOT FOUND")

    elif c == 4:
        FN =int(input("Enter the Flight Number of the Flight to be updated: "))
        sql = "DELETE FROM Flights WHERE FlightNum = {}".format(FN)
        try:
            cursor.execute(sql)
            mycon.commit()
            print("Flight removed successfully!")
        except:
            print("Flight NOT FOUND")
        D = input("Date of flight: ")
        TA = input("Time of Arrival: ")
        Des = input("The Destination: ")
        TD = input("Time of Departure: ")
        sql = "INSERT INTO Flights VALUES ({},'{}','{}','{}','{}')".format(FN,D,TA,Des,TD)
        try:
            cursor.execute(sql)
            mycon.commit()
            print("Flight added successfully")
        except:
            print("Incompatible values entered!")

    elif c == 5:
        cursor.execute("SELECT * FROM Flights")
        data = cursor.fetchall()
        print("Displaying the databse")
        for row in data:
            print(row)

    else:
        print("Please enter a valid choice")
    
#The User Menu in an infinite loop
while(True):
    print("Welcome to CS International Airport Flight Management System")
    print("Which Databse would you like to operate?")
    print("1. Passengers")
    print("2. Flights")
    print("3. Exit")
    ch = int(input("Enter the databse number: "))
    print()
    if ch == 1:
        Pass()
    elif ch == 2:
        Flig()
    elif ch == 3:
        print("Thank You for using the FMS!")
        break
    else:
        print("Please enter a valid number (1 to 3)")
    print("-----------------------------------------------------------------------")
