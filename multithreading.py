from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


obj1=hello()
obj2=hi()

obj1.start()   #start is equivalent to run bcz run is already in thread function
sleep(0.2)    #to wait for given time (in seconds)
obj2.start()

obj1.join()
obj2.join()

print("bye")