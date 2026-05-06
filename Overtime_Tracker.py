import json
from pathlib import Path

class OvertimeTracker:
    def __init__(self):
        hoursfile = Path("overtimehours.json")

        if hoursfile.exists():
            with open('overtimehours.json', 'r') as file:
                self.hours = json.load(file)
        else:
            self.hours = 0

    def addnew(self, value):
        self.hours += value

        with open('overtimehours.json', 'w') as file:
            json.dump(self.hours, file)

    def viewall(self):
        print(f"you have worked {self.hours} hours.")
    
    def targetpay(self):
        pay = int(input("How much do you get paid per hour?: "))

        targetpay = int(input("How much would you like to get paid this month?: "))

        hoursleft = round((targetpay - (self.hours * pay)) / pay, 2)

        if hoursleft > 0:
            print(f"you need to work {hoursleft} hours to attain that amount") 
        else:
            print(f"you have reached £ {targetpay} or more this month")




        


ot = OvertimeTracker()

ot.addnew(1)

ot.viewall()


print(ot.targetpay())

