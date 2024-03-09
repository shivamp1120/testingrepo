class Bankaccount:
    def __init__(self,name=None,typ=None,balance=None):
        self._name= name
        self._typ= typ
        self._balance= balance
        self._x=self._balance
    def inputs(self):
        self._name=input("Enter the name of account holder:")
        self._typ=input("Enter Account type:")
        self._balance=float(input("Enter balance:"))
        if self._x<=2000:
            print("your balance is less than 2000:")
        else:
            withdraw()
            show()

    def withdraw(self):
        self._wdamt=float(input("Enter withdraw amount:"))
        if self._wdamt+2000<self._balance:
            self._current=self._balance-self._wdamt
        else:
            print("Withdraw cannot be performed..")
            self._current=self._balance

    def deposit(self):
        self._depo=float(input("Enter deposit amount:"))
        self._current=self._balance+self._depo

    def show(self):
        print()
        print("Name:",self._name)
        print("Account type:",self._typ)
        print("current Balance:",self._current)

ob=Bankaccount()
ob.inputs()
ob.withdraw()
#ob.deposit()
ob.show()



