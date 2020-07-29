class BankAccount:
    ROI = 10.5
    #time for interest
    t = 5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Dispaly(self):
        print("Name: ", self.Name, "Amount: ", self.Amount)

    def Deposite(self,amount):
        self.Amount = self.Amount + amount

    def Withdraw(self, amount):
        self.Amount = self.Amount - amount

    def CalculateInterest(self, ROI, t):
        r = ROI/100
        self.Amount = self.Amount * (1 + (r * t))

def main():
    Obj1 = BankAccount("Sakshi", 50000)
    Obj1.Dispaly()

    Obj1.Deposite(500)
    Obj1.Dispaly()

    Obj1.Withdraw(500)
    Obj1.Dispaly()

    Obj1.CalculateInterest(10.5, 5)
    Obj1.Dispaly()

    Obj2 = BankAccount("Suhas", 10000)
    Obj2.Dispaly()

    Obj2.Deposite(500)
    Obj2.Dispaly()

    Obj2.Withdraw(500)
    Obj2.Dispaly()

    Obj2.CalculateInterest(10.5, 5)
    Obj2.Dispaly()

if __name__=="__main__":
    main()