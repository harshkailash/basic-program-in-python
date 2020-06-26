

class stu:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand="asus"
            self.cpu="i5"
            self.ram=16

        def show(self):
                print(self.brand,self.cpu,self.ram)



s1=stu('harsh',2)
s2=stu('arth',3)

s1.show()
lap1=s1.lap
s2.show()
lap2=s2.lap
