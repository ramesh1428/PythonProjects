import datetime
from  random import choice
from string import ascii_uppercase
class Booking:
    date = str(datetime.date.today())
    year = int(input("Enter year: "))
    while year < datetime.date.today().year:
        year = int(input("Enter year again: "))
    month = int(input("Enter month: "))
    while month < datetime.date.today().month:
        month = int(input("Enter month again: "))
    day = int(input("Enter day: "))
    while day < datetime.date.today().day:
        day = int(input("Enter day again: "))
    current_date = datetime.date(year, month, day)
    No_Of_Passengers = int(input("Select number of Passengers:"))
    while No_Of_Passengers <= 0:
        No_Of_Passengers = int(input("Select Valid number of Passengers "))
    arr_trains = [{"To": "Ngp", "From": "Kgp", "Train_No": 18517,"fare":550}, {"To": "Ngp", "From": "Kgp", "Train_No": 18112,"fare":700}]
    arr_pass = []
    arr_details = []
    if No_Of_Passengers >= 1:
        for i in range(1, No_Of_Passengers + 1):
            Name = input(f"Enter Name of Passenger {i}:")
            Age = int(input(f"Enter Age of Passenger {i}:"))
            Address = input(f"Enter Address of Passenger {i}:")
            Mob = str(input("Enter your Mobile number : "))
            while len(Mob) != 10 or Mob.startswith("0"):
                Mob = input("Enter your Mobile number again : ")
            arr_pass.append({f"Passenger {i}": {"Name": Name, "Age": Age, "Address": Address, "Mob": Mob}})
    def train_list(self):
        self.to_destination = input("Enter To destination :")
        self.from_destination = input("Enter From destination")
        for i in range(0, len(self.arr_trains)):
            if self.to_destination in self.arr_trains[i].values() and self.from_destination in self.arr_trains[i].values():
                print(f"{i+1}.Train Number {self.arr_trains[i].get('Train_No')} is available from {self.arr_trains[i].get('From')} to {self.arr_trains[i].get('To')}")

    def select_train(self):
        self.train_number=int(input("Enter train number :"))
        self.arr_details.append({"To":self.to_destination,"From":self.from_destination,"Train_Number":self.train_number})
        print(self.arr_details)
        print(f"Your Journey Destination- {self.arr_details[0].get('To')}")
        print(f"Your Journey From- {self.arr_details[0].get('From')}")
        print(f"Your Train number - {self.arr_details[0].get('Train_Number')}")
        with open("TrainTicket.txt", "a", encoding="utf-8")as f:
            f.write(f"Your Journey Destination- {self.arr_details[0].get('To')}\n")
            f.write(f"Your Journey From- {self.arr_details[0].get('From')}\n")
            f.write(f"Your Train number - {self.arr_details[0].get('Train_Number')}\n")
    def generate_pnr(self):
        self.pnr = f"PNR{''.join(choice(ascii_uppercase) for i in range(4))}S11{self.train_number}"
        print(f"Your Pnr number is: {self.pnr}")
        with open("TrainTicket.txt", "a", encoding="utf-8") as f:
            f.write(f"Your Pnr number is: {self.pnr}\n")
    def train_fare(self):
        self.pass_fare=0
        arr_fare=[]
        total_fare=0
        for i in range(0,len(self.arr_trains)):
            if self.train_number in self.arr_trains[i].values():
                self.pass_fare=self.arr_trains[i].get("fare")
        #print(self.pass_fare)
        for i in range(0,len(self.arr_pass)):
            if self.arr_pass[i][f"Passenger {i+1}"].get("Age")>=60:
                arr_fare.append(self.pass_fare/2)
            elif self.arr_pass[i][f"Passenger {i+1}"].get("Age")<=2:
                arr_fare.append(self.pass_fare / 4)
            else:
                arr_fare.append(self.pass_fare)
        for i in range(0,len(arr_fare)):
            total_fare=total_fare+arr_fare[i]
        #print(arr_fare)
        print(f"Your total fare for the journey from {self.from_destination} to {self.to_destination} in train number {self.train_number} is ₹{total_fare}")
        with open("TrainTicket.txt", "a", encoding="utf-8")as f:
            f.write(f"Your total fare for the journey from {self.from_destination} to {self.to_destination} in train number {self.train_number} is ₹{total_fare}\n")

New_Booking = Booking()
New_Booking.train_list()
New_Booking.select_train()
New_Booking.generate_pnr()
New_Booking.train_fare()

#print(New_Booking.arr_pass)