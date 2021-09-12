import math
def hello():
    print ('Варіант 27, програма для обчислення y в залежності від значення х')
    print('Чумак С.І., група КМ-12')

def read_x():
    x=float(input('Введіть значення х='))
    return x

def calculate_y(x):
    if x<-1.5 :
        y=math.pi*math.sin(x)
    else :
        if x>=2.5 :
            y=math.pi*x
        else :
            y=x*math.sin(x)
    return y

if __name__ == "__main__":
    # execute only if run as a script
    hello()
    while True:
        try:
            x=read_x()
            y=calculate_y(x)
            print ("При значенні х = %f y = %f." % (x,y))
            break
        except Exception as e:
            print (e)



