import math
def hello():
    print ('Варіант 27, програма для обчислення кутів трикутника з його сторін.')
    print('Чумак С.І., група КМ-12')

def read_abc():
    print ('Введіть сторони a,b,c трикутника')
    a=int(input())
    b=int(input())
    c=int(input())
    if a+b>c and b+c>a and a+c>b and a>0 and b>0 and c>0:
        return (a,b,c)
    raise 
def angle(a,b,c):
    r=math.acos((a*a+b*b-c*c)/(2*a*b))
    g=r/math.pi*180
    return (r,g)


if __name__ == "__main__":
    # execute only if run as a script
    hello()
    while True:
        try:
            (x,y,z) = read_abc()
            print(x,y,z)
            (fr,fg)=angle(x,y,z)
            (gr,gg)=angle(y,z,x)
            (hr,hg)=angle(z,x,y)
            print("Кут %s в радіанах = %f , в градусах = %f " % ("F", fr, fg))
            print("Кут %s в радіанах = %f , в градусах = %f " % ("G", gr, gg))
            print("Кут %s в радіанах = %f , в градусах = %f " % ("H", hr, hg))
            break
        except :
            print("wrong")