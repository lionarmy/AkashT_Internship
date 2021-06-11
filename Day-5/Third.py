def display(si):
    print(si)


class Cal3: 

    def _init_(self):
        self.p = int(input("Enter P:"))
        self.r = int(input("Enter R:"))
        self.t = int(input("Enter T:"))

    def callInterest(self):
        si = (self.p * self.r * self.t)/100
        display(si)



obj = Cal3()
obj.callInterest()