
def hello():
     print ('Варіант 27, чи пройде цеглина через отвір?')
     print('Чумак С.І., група КМ-12')

def read_AB():
    print('Введіть сторони A,B отвору')
    A=float(input('A='))
    B=float(input('B='))
    if A>0 and B>0 :
        return (A,B)
    raise Exception('Неіснуючі розміри отвору.')

def read_xyz():
    print('Введіть параметри x,y,z цеглини')
    x=float(input('x='))
    y=float(input('y='))
    z=float(input('z='))
    if x>0 and y>0 and z>0 :
        return (x,y,z)
    raise Exception('Неіснуючі розміри цеглини.')


if __name__ == "__main__":
    # execute only if run as a script
    hello()
    while True:
        try:
            (w,h)=read_AB()
            (a,b,c)=read_xyz()
            (w,h)=sorted((w,h))
            (a,b,c) = sorted((a,b,c))
            print ("Розміри отвору %f x %f , розміри цеглини %f x %f " % (w,h,a,b))
            if w>a and h>b :
                print ('Цеглина пройде.')
            else :
                print ('Цеглина не пройде')
            break
        except Exception as e :
            print(e)