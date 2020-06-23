def ten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1


values=ten()

for i in values:
    print(i)