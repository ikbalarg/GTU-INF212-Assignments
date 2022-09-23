#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:53:43 2022

@author: ikbalarguc
"""

my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
import random ,string, time,heapq
#Problem 1
def problem1(x,q=1,z=10,y=0):
    sizeOfList=x
    entryType=y
    list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
           "p","q","r","s","t","u","v","w","x","y","z","A","B","C","D",
           "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S",
           "T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
    out=[]
    if entryType==0:
        for i in range(sizeOfList):
            sayi=random.randint(q, z)
            print(sayi)
            str1=""
            for i in range(sayi):
                str1=str1+random.choice(list1)
            out.append(str1)
            str1=""
    elif entryType==1:
        for i in range(sizeOfList):
            out.append(random.randint(q,z))
    elif entryType==2:
        for i in range(sizeOfList):
            out.append(random.uniform(q, z))
    return out
#Problem2
def problem2(x):
    baslangıc=time.perf_counter_ns()
    indexler=range(1,len(x))
    for i in indexler:
        deger=x[i]
        while x[i-1]>deger and i>0:
            x[i],x[i-1] = x[i-1],x[i]
            i=i-1
    son=time.perf_counter_ns()
    return son-baslangıc
#Problem3
def problem3(x):
    baslangic=time.perf_counter_ns()
    indisler=range(1,len(x))
    for i in indisler:
        while x[i-1]>x[i] and i>0:
            d1=x[i]
            d2=x[i-1]
            x.pop(i-1)
            x.insert(i-1,d1)
            x.pop(i)
            x.insert(i,d2)
            i=i-1
    son=time.perf_counter_ns()
    return son-baslangic
#Problem4
def problem4(alist):
    baslangic=time.perf_counter_ns()
    def binary_search(alist, key, start, end):
        if end - start <= 1:
            if key < alist[start]:
                return start - 1
            else:
                return start
     
        mid = (start + end)//2
        if alist[mid] < key:
            return binary_search(alist, key, mid, end)
        elif alist[mid] > key:
            return binary_search(alist, key, start, mid)
        else:
            return mid 
    for i in range(1, len(alist)):
           temp = alist[i]
           pos = binary_search(alist, temp, 0, i) + 1
    
           for k in range(i, pos, -1):
               alist[k] = alist[k - 1]
    
           alist[pos] = temp
    son=time.perf_counter_ns()
    return son-baslangic
#Problem5
def problem5(x):
    baslangic=time.perf_counter_ns()
    if len(x) > 1:
        r = len(x)//2
        L = x[:r]
        M = x[r:]
        problem5(L)
        problem5(M)
        i =0
        j =0
        k =0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                x[k] = L[i]
                i += 1
            else:
                x[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            x[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            x[k] = M[j]
            j += 1
            k += 1
    son=time.perf_counter_ns()
    return son-baslangic
            
#Problem6
def problem6(x):
    baslangic=time.perf_counter_ns()
    liste=[]
    for i in x:
        heapq.heappush(liste, i)
    son=time.perf_counter_ns()
    return [heapq.heappop(liste) for i in range(len(liste))],son-baslangic
            

            
        
        
