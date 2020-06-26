a=5
b=2

try:
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("you cannot divide a number by 0")
    print("resource closed")
except ValueError:
    print("invalid input")
except Exception:
    print("something went wrong")
finally:
    print("resource closed")