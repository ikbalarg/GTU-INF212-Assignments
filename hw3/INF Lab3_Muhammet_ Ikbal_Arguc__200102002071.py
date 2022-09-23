my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
import numpy as np
import random
#problem1
def problem1(c1,c2,operation):
    operation=operation.lower()
    complex1=c1#complex(''.join(c1.split()))
    complex2=c2#complex(''.join(c2.split()))
    if operation=="mul":
        return np.multiply(complex1,complex2)
    elif operation=="add":
        return np.add(complex1,complex2)
    elif operation=="div":
        return np.divide(complex1,complex2)
    elif operation=="sub":
        return np.subtract(complex1,complex2)
    else:
        return None
#problem2
def problem2(c1,operation):
    operation=operation.lower()
    if operation=="abs":
        return float(np.absolute(c1))
    elif operation=="ang":
        return float(np.angle(c1))
    elif operation=="pol":
        return (float(np.absolute(c1)),float(np.angle(c1)))
    elif operation=="con":
        return np.conj(c1)
    else:
        return None
#problem3
def problem3(row,column,emin,emax):
    a1=np.random.uniform(size = (row,column), low = emin, high = emax)
    a2=np.random.uniform(size = (row,column), low = emin, high = emax)*1j
    return a1+a2
#problem4
def problem4(row,emin,emax):
    a1=np.random.uniform(size = (row), low = emin, high = emax)
    a2=np.random.uniform(size = (row), low = emin, high = emax)*1j
    return a1+a2
#problem5
def problem5(Mat,alpha):
    a1=np.diag(np.diag(Mat))
    a1=alpha+a1
    uzunluk1=len(Mat)
    sayi1=0
    for i in range(uzunluk1):
        k=a1[sayi1][sayi1]
        Mat[sayi1][sayi1]=k
        sayi1+=1
    return Mat
def problem6(d1,d2):
    try:
        return np.linalg.solve(d1, d2)
    except:
        return None
#problem7
def problem7(x):
    try:
        inverse = np.linalg.inv(x)
    except:
        return None
    return inverse
#problem8
def problem8(a,b):
    try:
        inversea= np.linalg.inv(a)
        inverseb = np.linalg.inv(b)
    except np.linalg.LinAlgError:
        return None
    if inversea.all()==b.all() or inverseb.all()==a.all():
        return True
    else:
        return False
#problem9
def problem9(mat,vec):
    try:
        return np.dot(mat,vec)
    except :
        return None
#problem10
def problem10(mat,string):
    s1=string.lower()
    try:
        if s1=="det":
            return np.linalg.det(mat)
        elif s1=="rank":
            return np.linalg.matrix_rank(mat)
        elif s1=="eig":
            w, v = np.linalg.eig(mat)
            return w
        elif s1=="eigvec":
            w, v = np.linalg.eig(mat)
            return (w,v)
        elif s1=="svd":
            u, s, vh = np.linalg.svd(mat)
            return u,s,vh
        else:
            return None
    except:
        return None
