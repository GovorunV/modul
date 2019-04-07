if __name__=="__main__": #это конгда должно выполняться только в этом файлу
    print("hello")


some = 12
def printfd(str):
    print("res",str)

def summ(*args):
    sum=0
    for i in args:
        sum+=i
    return sum