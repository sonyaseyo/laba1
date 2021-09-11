
def hello():
     print ('Варіант 27, чи пройде цеглина через отвір?')
     print('Чумак С.І., група КМ-12')

def read_AB():
    print('Введіть сторони A,B отвору')
    A=float(input())
    B=float(input())
    if A>0 and B>0 :
        return (A,B)
    raise

def read_xyz():
    print('Введіть параметри x,y,z цеглини')
    x=float(input())
    y=float(input())
    z=float(input())
    if x>0 and y>0 and z>0 :
        return (x,y,z)
    raise

def min2(A,B):
    if A<B :
       return (A,B)
    else :
       return (B,A)

def min3to2(x,y,z): 
    (x,y)=min2(y,x)
    (y,z)=min2(y,z)
    (x,y)=min2(y,x)
    return (x,y)
   

if __name__ == "__main__":
    # execute only if run as a script
    hello()
    while True:
        try:
            (w,h)=read_AB()
            (a,b,c)=read_xyz()
            (w,h)=min2(w,h)
            (a,b) = min3to2(a,b,c)
            print ("Розміри отвору %f x %f , розміри цеглини %f x %f " % (w,h,a,b))
            if w>a and h>b :
                print ('Цеглина пройде.')
            else :
                print ('Цеглина не пройде')
            break
        except : 
               print ('wrong')
                