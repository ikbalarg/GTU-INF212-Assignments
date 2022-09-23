my_name="Muhammet İkbal Arğuç"
my_id="200102002071"
my_email="m.arguc2020@gtu.edu.tr"
#Project1
import bstgtu as bst
import avlgtu as avl
import time
def reltime(t,tbase='070000'):
    x=int(t)-int(tbase)
    if len(str(x))==5:
        a=int(str(x)[0])*60*60
        b=int(str(x)[1:3])*60
        c=int(str(x)[3:])
        return a+b+c
    elif len(str(x))==6:
        a=int(str(x)[0:2])*60*60
        b=int(str(x)[2:4])*60
        c=int(str(x)[4:])
        return a+b+c
    elif len(str(x))==3 or len(str(x))==4:
        a=int(str(x)[-2:])
        b=int(str(x)[:-2])*60
        return a+b
    elif len(str(x))==2 or len(str(x))==1:
        return x
    
    
def read2tree(filename, TreeType,tbase='070000', tceil='220000'):
    liste=[]
    asil=[]
    degerler=[]
    okuma = open(filename).readlines()
    for i in okuma:
        liste.append(i[0:6])
        degerler.append(i[10:-1])
    count=0
    for i in liste:
        if i <=tceil and tbase<=i:
            a=reltime(t=i,tbase=tbase)
            asil.append(a)
        else:
            continue
    if TreeType== "BST":
        a=bst.BST()
        for i in asil:
            a.insert(i).set_gtu(degerler[count])
            count+=1
        return a
    elif TreeType=="AVL":
        a=avl.AVL()
        print(degerler)
        for i in asil:
            a.insert(i)
            a.find(i).set_gtu(degerler[count])
            #a.root.set_gtu(degerler[count])
            count+=1
        return a
def maximum(node):
    current = node.root
    while current.right is not None:
        current = current.right
    return current
def predecessor(node):
    def maxic(node):
        current = node
        while current.right is not None:
            current = current.right
        return current
    if node.left is not None:
        return maxic(node.left)
    current = node
    while current.parent is not None and current.parent.left is current:
        current = current.parent
    return current.parent
def dyna_int_updater(IntValue,tdo,tup,innode,nxsmaller,nxlarger):
    innode1=float(innode.get_gtu())
    if nxsmaller!=None and nxlarger!=None:
        nxsmaller1=float(nxsmaller.get_gtu())
        nxlarger1=float(nxlarger.get_gtu())
        if nxsmaller1<tdo and tdo<innode1:
            nxsmaller1=tdo
        if nxlarger1>tup and tup>innode1:
            nxlarger1=tup
        deger=IntValue+(nxlarger1-innode1)*(innode1-nxsmaller1)
        return float(deger)
    elif nxlarger==None and nxsmaller!=None:
        nxsmaller1=float(nxsmaller.get_gtu())
        nxlarger1=tup
        deger=IntValue+(nxlarger1-innode1)*(innode1-nxsmaller1)
        return float(deger)
    elif nxlarger!=None and nxsmaller==None:
        nxlarger1=float(nxlarger.get_gtu())
        nxsmaller1=tdo
        deger=IntValue+(nxlarger1-innode1)*(innode1-nxsmaller1)
        return float(deger)
def GTU_tree_rad_calc(MTree,tlo=None, thi=None, tbase="070000", tceil="220000"):
    t1=time.perf_counter_ns()
    liste=[]
    kontrol=MTree.root
    b=maximum(MTree)
    a=kontrol.minimum()
    liste.append(a)
    while b!=a:
        a=a.successor()
        liste.append(a)
    if tlo==None:
        tlo=tbase
    if thi==None:
        thi=tceil
    integralDeger1=float(reltime(tlo))
    integralDeger2=float(reltime(thi))
    hesaplamalar=[]
    count1=2
    num=0
    liste2=liste.copy()
    for a in liste:
        if float(a.key)>=integralDeger1:
            if float(a.key)>integralDeger2:
                break
            else:
                count=count1
                if a.key == liste2[0].key:
                    hesaplamalar.append(((float((liste2[1].key))-integralDeger1)*float(liste2[0].gtu))/3600)
                elif a.key==liste[1].key:
                    hesaplamalar.append(((float(liste2[2].key)-float(liste2[1].key))*float(liste2[1].gtu)+(float(liste2[1].key)-integralDeger1)*float(liste2[0].gtu))/3600)
                else:
                    deger1=(float(liste2[1].key)-integralDeger1)*float(liste2[0].gtu)
                    if a.key != b.key:
                        
                        deger2=(float(liste2[count+1].key)-float(liste2[count].key))*float(liste2[count].gtu)
                    else:
                        deger2=(float(integralDeger2)-float(liste2[count].key))*float(liste2[count].gtu)
                    aratoplam=0
                    while count>1:
                        count=count-1
                        x=float((liste2[count+1].key)-float(liste2[count].key))*float(liste2[count].gtu)
                        aratoplam+=x
                    hesaplamalar.append((deger1+deger2+aratoplam)/3600)
                    aratoplam=0
                    count1+=1
        else:
            liste2.pop(0)
            count1=count1-1
        num+=1
    t2=time.perf_counter_ns()
    return hesaplamalar[-1],hesaplamalar,t2-t1
                
            
def GTU_int_calc(filename, TreeType,tlo=None, thi=None,tbase="070000", tceil="220000"):
    t1=time.perf_counter_ns()
    if tlo==None:
        tlo=float(reltime(tbase))
    else:
        tlo=float(reltime(tlo))
    if thi==None:
        thi=float(reltime(tceil))
    else:
        thi=float(reltime(tceil))
    integralAlt=(tlo)
    integralUst=(thi)
    liste=[]
    asil=[]
    degerler=[]
    okuma = open(filename).readlines()
    for i in okuma:
        liste.append(i[0:6])
        degerler.append(i[10:-1])
    count=0
    for i in liste:
        a=reltime(t=i,tbase=tbase)
        asil.append(a)
    if TreeType== "BST":
        a=bst.BST()
        aradeger=0
        integraller=[]
        agac=[]
        for i in asil:
            a.insert(i).set_gtu(degerler[count])
            b=a.find(i)
            if b.key==a.root.key:
                integraller.append(((float(integralUst)-float(integralAlt))*float(b.gtu))/3600)
                aradeger=aradeger+((float(integralUst)-float(integralAlt))*float(b.gtu))/3600
            elif b.key==a.root.minimum().key:
                integralUst=b.successor().key
                integralAlt=b.key
                integraller.append(aradeger-((float(integralUst)-float(integralAlt))*float(b.successor().gtu))/3600)
                aradeger=aradeger-(((float(integralUst)-float(integralAlt))*float(b.successor().gtu))/3600)
            elif b.key==maximum(a).key:
                integralAlt=(b.find(b.key))
                integralUst=thi
                integraller.append(aradeger+((float(integralUst)-float(integralAlt.key))*(float(b.gtu)-float((predecessor(b.find(b.key))).gtu))/3600))
                aradeger=aradeger+((float(integralUst)-float(integralAlt.key))*(float(b.gtu)-float((predecessor(b.find(b.key))).gtu))/3600)
            else:
                integralAlt=b.key
                integralUst=b.successor().key
                integraller.append(aradeger+((float(integralUst)-float(integralAlt))*((float(b.gtu))-float(((predecessor(b).gtu))))/3600))
                aradeger=aradeger+((float(integralUst)-float(integralAlt))*((float(b.gtu))-float(((predecessor(b).gtu))))/3600)
            count+=1
        t2=time.perf_counter_ns()
        return aradeger,integraller,t2-t1
    elif TreeType=="AVL":
        a=avl.AVL()
        aradeger=0
        integraller=[]
        agac=[]
        for i in asil:
            print(degerler[count])
            a.insert(i)
            a.find(i).set_gtu(degerler[count])
            b=a.find(i)
            if b.key==a.root.key:
                integraller.append(((float(integralUst)-float(integralAlt))*float(b.gtu))/3600)
                aradeger=aradeger+((float(integralUst)-float(integralAlt))*float(b.gtu))/3600
            elif b.key==a.root.minimum().key:
                integralUst=b.successor().key
                integralAlt=b.key
                integraller.append(aradeger-((float(integralUst)-float(integralAlt))*float(b.successor().gtu))/3600)
                aradeger=aradeger-(((float(integralUst)-float(integralAlt))*float(b.successor().gtu))/3600)
            elif b.key==maximum(a).key:
                integralAlt=(b.find(b.key))
                integralUst=thi
                integraller.append(aradeger+((float(integralUst)-float(integralAlt.key))*(float(b.gtu)-float((predecessor(b.find(b.key))).gtu))/3600))
                aradeger=aradeger+((float(integralUst)-float(integralAlt.key))*(float(b.gtu)-float((predecessor(b.find(b.key))).gtu))/3600)
                
            else:
                integralAlt=b.key
                integralUst=b.successor().key
                integraller.append(aradeger+((float(integralUst)-float(integralAlt))*((float(b.gtu))-float(((predecessor(b).gtu))))/3600))
                aradeger=aradeger+((float(integralUst)-float(integralAlt))*((float(b.gtu))-float(((predecessor(b).gtu))))/3600)
            count+=1
        t2=time.perf_counter_ns()
        return aradeger,integraller,t2-t1
def GTU_tree_dyna_add(filename, MTree,IntValue=0, tlo=None, thi=None,tbase="070000", tceil="220000"):
    pass

        
        
    
        
    
                         

                
    
        
            
        