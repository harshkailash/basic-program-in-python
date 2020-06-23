class stu:
    school="cms"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    

s1=stu(34,47,32)
s2=stu(89,32,12)

print(s1.avg())
