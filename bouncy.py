def decrease(num):
    ls1=[]
    ls=[int(x) for x in num]
    for i in range(0,len(ls)):
        ls1.append(ls[i]) 
    ls.sort(key=int)
    if(ls1==ls) :
        return True
    else:
        return False

def increase(num):
       ls1=[]
       ls=[int(x) for x in num]
        for i in range(0,len(ls)):
            ls1.append(ls[i])
        ls.sort(key=int)
        if(ls1[::-1]==ls) :
            return True
        else:
            return False

i=100
count=0
while True:
    if((increase(i)== False) and (decrease(i)== False)):
        count+=1
    if ((i*0.99) == count) :
            print(i)
            break
    i+=1

