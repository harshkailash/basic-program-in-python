class cars:

    wheels=4


    def __init__(self):
        self.mil=10
        self.com="bmw"
c1=cars()
c2=cars()

c1.mil=9

cars.wheels=5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
