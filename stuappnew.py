class Student:
    def __init__(self):
        self._roll = None
        self._name = None
        self._marks = None
    def input(self):
        
        self._roll = int(input("\nRoll : "))
        self._name = input("Name : ")
        s1 = float(input("Hindi : "))
        s2 = float(input("English : "))
        s3 = float(input("Maths : "))
        s4 = float(input("Science : "))
        s5 = float(input("Computer : "))
        self._marks = {"hindi":s1,"english":s2,"maths":s3,"science":s4,"computer":s5}
    def show(self):
        print("\nRoll : ", self._roll)    
        print("Name : ", self._name)    
        print("Subject Marks : ")
        for item in self._marks.items():
            print("\t",item[0].title() , " : " , item[1])
    def getTotalMarks(self):
        return sum(self._marks.values())
    def getRoll(self):
        return self._roll

       
#*********************************************************
   
students = []


while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Student List")
    print("4. Get Topper")
    print("5. get maths topper")
    print("6. Exit")
    choice = int(input(">>> "))
    if choice==6:
        break
    elif choice==1:
        ob = Student()
        ob.input()
        for stu in students:
            if stu.getRoll()==ob.getRoll():
                print("Duplicate Rollno not allowed.")
                break;
        else:
            students.append(ob)
            print("** Student Added ! **") 
    elif choice==2:
        roll = int(input("\nRoll : ")) 
        for ob in students:
            if ob.getRoll()==roll:
                ob.show()
                break
        else:
            print("** Student Not Found !**")    
    elif choice==3:
        if len(students)==0:
            print("** No student in list !**")
        else:
            for ob in students:
                ob.show()     
    elif choice==4:
        if len(students)==0:
            print("** No student in list !**")
        else:    
            stud = None
            for ob in students:
                if stud is None:
                    stud=ob
                elif ob.getTotalMarks() > stud.getTotalMarks():
                    stud=ob 
            stud.show() 
   
    elif choice==5:
        if len(students)==0:
            print("** No student in list !**")
        else:    
            stud = None
            for ob in students:
                if stud is None:
                    stud=ob
                elif ob.getTotalMarks() > stud.getTotalMarks():
                    stud=ob 
            stud.show()
    else:
        print("** Wrong Input !**")

# choice==1: Roll Duplicate Not Allowed !
# Get Maths Topper
# List Student Science > Computer
# Bottom 2 Student ....
  
# lis=[10,20,30,40,20,50,60,40]
# uni=set(lis)
# lis=(list(uni))
# print(lis)