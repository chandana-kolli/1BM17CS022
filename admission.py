class admission:
    def __init__(self):
        self.stu_id=None
        self.age=None
        self.marks=None
    def set(self,sid,ag,mr):
        self.stu_id=sid
        self.age=ag
        self.marks=mr
        self.validate()
    def validate(self):
        if(self.age>20 and self.marks>0 and self.marks<100):
            self.check_qualifications()
            #return True
        else:
            print("data is not valid")
            #return False
    def check_qualifications(self):
        #a=self.validate()
        if(self.marks>=65):
            self.get()
            #return True
        else:
            print(self.stu_id," is not qualified for admission")
            #return False
    def get(self):
        print("You are admitted")
        print("Student ID: ",self.stu_id)
        print("Student age: ",self.age)
        print("Student marks: ",self.marks)
n=int(input("How many students"))
li=[]
for i in range(n):
    print("Enter student id,age and marks")
    idd=int(input())
    age=int(input())
    marks=int(input())
    li.append(admission().set(idd,age,marks))
    




            
