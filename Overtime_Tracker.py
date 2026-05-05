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
        


ot = OvertimeTracker()

ot.addnew(2)

ot.viewall()

