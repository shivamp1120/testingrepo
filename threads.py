from threading import Thread
class Dad(Thread):
    def __init__(self,num):
        super().__init__()
        self.num=num
    def run(self):
        print("father class:",self.num)

class Son(Dad):
    def __init__(self,a,num):
        super().__init__(num)
        self.a=a
    def run(self):
        super().run()
        print("son class:",self.a)

ob=Son(45,50)
ob1=Son(60,70)
ob.start()
ob1.start()
