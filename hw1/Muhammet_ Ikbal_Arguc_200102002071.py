my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
import random
#Problem1
def problem1(x):
    bl=[]
    for i in range(x):
        bl.append(random.randint(0,1000))
    return bl
#Problem2
def problem2(x,y):
    l1=[]
    for i in range(x):
        l2=[]
        for i in range(y):
            l2.append(random.randint(0, 1000))
        l1.append(l2.copy())
        l2.clear()
    return l1
#Problem3
def problem3(x,y=[]):
    if type(y)==list:
        indeks=round(len(x)/2)
    else:
        indeks=y
    kontrol=False
    if y==0:
        if x[0]>x[1]:
            return (x[0],[y])
        indeks=0
        a=[0]
        while kontrol==False:
            check=(indeks+1)!=len(x)
            if check==True:
                if x[indeks]>=x[indeks+1] and x[indeks]>=x[indeks-1]:
                    print("Girildi")
                    if (indeks+1)!=len(x):
                        print(a)
                        y=a
                        return (x[indeks],a[-1]),a
                else:
                    indeks+=1
                    a.append(indeks)
                    print(indeks)
            elif check==False:
                return (x[indeks],a[-1]),a
    else:
        d=[indeks]
        if x[indeks]>=x[indeks+1] and x[indeks]>=x[indeks-1]:
            d.append(indeks)
            return (x[indeks],d[-1]),d
        else:
            while True:
                check=(indeks+1)!=len(x)
                #print(indeks)
                #print(check)
                if check==True:
                    if  x[indeks]>=x[indeks+1] or indeks==len(x)-1:
                        print(1)
                        indeks=indeks-1
                        if x[indeks]>=x[indeks+1] and x[indeks]>=x[indeks-1]:
                            print(4)
                            d.append(indeks)
                            return (x[indeks],d[-1]),d
                        else:
                            d.append(indeks)
                    else:
                        print(2)
                        indeks=indeks+1
                        try:
                            if x[indeks]>=x[indeks+1] and x[indeks]>=x[indeks-1]:
                                print(3)
                                d.append(indeks)
                                return (x[indeks],d[-1]),d
                            else:
                                d.append(indeks)
                        except IndexError:
                            continue
                elif check==False:
                    d.append(indeks)
                    return (x[indeks],d[-1]),d
#Problem4
def problem4():
    pass
"""
if y==None:
    indeks=round(len(x)/2)
else:
    indeks=y
d=[]
if indeks!=0 or indeks!=(len(x)-1) :
    if x[indeks]>=x[indeks+1] and x[indeks]>=x[indeks-1]:
        d.append(indeks)
        return (x[indeks],d[-1]),d
    else:
       while True:
        #for i in range(4)   :
            d.append(indeks)
            print(d)
            if x[indeks]<x[indeks-1]:
                
                #x=x[0:indeks-1].copy()
                leng=len(x[:(indeks-1)])
                
                indeks=round((leng/2))
                print(indeks)
                if x[indeks]>=x[indeks+1] and x[indeks]>=x[indeks-1]:
                    d.append(indeks)
                    return (x[indeks],d[-1]),d
                else:
                    continue
            elif x[indeks]<x[indeks+1]: 
                indeks=round((indeks+(len(x)))/2)
                print(indeks)
                if indeks==len(x)-1:
                    d.append(indeks)
                    return (x[indeks],d[-1]),d
                else:
                    
                    if x[indeks]>=x[indeks+1] and x[indeks]>=x[indeks-1]:
                        d.append(indeks)
                        return (x[indeks],d[-1]),d
                    else:
                        continue
"""
#Problem5
def problem5(x,y=None,z=None):
    if y == None:
        n=round(len(x)/2)
    else:
        n=y
    if z==None:
        m = round(len(x[0])/2)
    else:
        m=z
    l1=[[n,m]]
    try:
        if x[n][m]>=x[n+1][m] and x[n][m]>=x[n][m+1] and x[n][m]>=x[n-1][m] and x[n][m] >= x[n][m-1]:
            return (x[n][m],l1[-1]),l1
    except:
        next
    while True:
        print("Döngü")
        if n!=0 and x[n-1][m]>=x[n][m]:
            n=n-1
        elif m!=0 and x[n][m-1]>=x[n][m]:
            m=m-1
        elif n!=len(x)-1 and x[n+1][m]>=x[n][m]:
            n=n+1
        elif m!=len(x[0])-1 and x[n][m+1]>=x[n][m]:
            m=m+1
        l1.append([n,m])
        try:
            if n==(len(x)-1):
                if m==len(x[0])-1 and x[n][m]>=x[n-1][m] and x[n][m] >= x[n][m-1]:
                    return (x[n][m],l1[-1]),l1
                elif m!=0 and m!=len(x[0])-1 and x[n][m]>=x[n-1][m] and x[n][m]>=x[n][m+1]:
                    return (x[n][m],l1[-1]),l1
                elif m==0 and x[n][m]>=x[n-1][m] and x[n][m]>=x[n][m+1]:
                    return (x[n][m],l1[-1]),l1
            elif n==0:
                if m!=0 and m!=len(x[0])-1 and x[n][m]>=x[n+1][m] and x[n][m]>=x[n][m+1]:
                    return (x[n][m],l1[-1]),l1
                elif m==len(x[0])-1 and x[n][m]>=x[n+1][m] and x[n][m] >= x[n][m-1]:
                    return (x[n][m],l1[-1]),l1
                elif m==0 and x[n][m]>=x[n+1][m] and x[n][m]>=x[n][m+1]:
                    return (x[n][m],l1[-1]),l1
            elif m==len(x[0])-1:
                if n==(len(x)-1) and x[n][m]>=x[n-1][m] and x[n][m] >= x[n][m-1]:
                    return (x[n][m],l1[-1]),l1
                elif n!=(len(x)-1) and x[n][m]>=x[n+1][m] and x[n][m]>=x[n-1][m] and x[n][m] >= x[n][m-1]:
                    return (x[n][m],l1[-1]),l1
                elif n==0 and x[n][m]>=x[n+1][m] and x[n][m] >= x[n][m-1]:
                    return (x[n][m],l1[-1]),l1
            elif m==0:
                if n!=0 and n!=len(x[0])-1 and x[n][m]>=x[n+1][m] and x[n][m]>=x[n][m+1]:
                    return (x[n][m],l1[-1]),l1
                elif n==len(x[0])-1 and x[n][m]>=x[n-1][m] and x[n][m] >= x[n][m+1]:
                    return (x[n][m],l1[-1]),l1
                elif n==0 and x[n][m]>=x[n+1][m] and x[n][m]>=x[n][m+1]:
                    return (x[n][m],l1[-1]),l1
            elif x[n][m]>=x[n+1][m] and x[n][m]>=x[n][m+1] and x[n][m]>=x[n-1][m] and x[n][m] >= x[n][m-1]:
                return (x[n][m],l1[-1]),l1
            
        except:
            next
def problem6():
    pass