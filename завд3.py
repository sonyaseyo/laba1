import math
def hello():
    print ('Варіант 27, програма для обчислення y в залежності від значення х')
    print('Чумак С.І., група КМ-12')

def read_x():
    print ('Введіть значення х')
    x=float(input())
    return x

def calculate_y():
    x=read_x()
    if x<-1.5 :
        y=math.pi*math.sin(x)
    else :
        if x>=2.5 :
            y=math.pi*x
        else :
            y=x*math.sin(x)
    return y

def result(x,y):
    print ("При значенні х = %f y = %f"%(x,y))


