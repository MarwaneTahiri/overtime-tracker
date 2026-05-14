import json
from pathlib import Path


class OvertimeTracker:
    def __init__(self):
        self.overtimelist = []


        hoursfile = Path("overtimehours.json")

        if hoursfile.exists():
            with open('overtimehours.json', 'r') as file:
                self.overtimelist = json.load(file)
        else:
            self.overtimelist = []
            

    def addnew(self):
        overtimedate = input("When was this? DD-MM-YY: ")
        overtimehours = input("How many hours would you log?: ")

        while not overtimehours.isdigit():
            overtimehours = input("Enter number only, How many hours would you log?: ")
        else:
            self.overtimelist.append({overtimedate: int(overtimehours)})
        

        

        with open('overtimehours.json', 'w') as file:
            json.dump(self.overtimelist, file)


    def viewallhours(self):
        print(f"You have worked {self.totalhours()} hours.")
    
    def viewallentries(self):
        if not self.overtimelist:
            print("No overtime has been logged yet.")
        else:
            for entry in self.overtimelist:
                for date, hours in entry.items():
                    print(f"{date}: {hours}")

    def targetpay(self):
        pay = int(input("How much do you get paid per hour?: "))

        targetpay = int(input("How much would you like to get paid this month?: "))

        hoursleft = round((targetpay - (self.totalhours() * pay)) / pay, 2)

        if hoursleft > 0:
            print(f"you need to work {hoursleft} more hours to attain that amount") 
        else:
            print(f"you have reached £ {targetpay} or more this month")

    def totalhours(self):
        self.total = 0
        
        for dicts in self.overtimelist:
            for j in dicts.values():
                self.total = self.total + j 
        return self.total






ot = OvertimeTracker()

while True:
    choice = input("1. Log overtime\n 2. View total hours\n 3. View all entries\n 4. Target pay calculator\n 5. Exit\n Enter Number: ")

    if choice == "1":
        ot.addnew()
    
    elif choice == "2":
        ot.viewallhours()

    elif choice == "3":
        ot.viewallentries()

    elif choice == "3":
        ot.targetpay()

    elif choice == "4":
        break


