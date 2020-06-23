class pycharm:
    def exec(self):
        print("compiling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.exec()

ide=pycharm()

lap1=Laptop()
lap1.code(ide)
