r = int(input("enter rows:"))
c = int(input("enter columns:"))
b="."
lr2=[]
for i in range(0,r):
    i = input()
    if len(i) != c:
        print("please try again")
        break
    else:
      lr1 = list(i)
      lr2.append(lr1)      
#number()
ls=[]
ls1=[]
ls2=[]
i=1
for x in range(0,r) :
    for y in range(0,c) :
        if x==0 :
            if ("*" not in lr2[x][y]):
                ls.append(i)
                i+=1
            else:
                ls.append(ls2)    
              
        elif y==0 :
            if ("*" not in lr2[x][y]) :
                if ("*" in lr2[x-1][y] or "*" in lr2[x+1][y]) :
                    ls.append(i)      
                    i+=1
            else:
                ls.append(ls2)
            
        else :
             if ("*" not in lr2[x][y] ) :
                 if ("*" in lr2[x-1][y] or "*" in lr2[x][y-1]):
                     ls.append(i)
                     i+=1
                 elif("*" not in lr2[x-1][y] and "*" not in lr2[x][y-1]):
                     ls.append(ls2)
             else:
                 ls.append(ls2)
                
    ls1.append(ls)
    ls=[]
if(r==c):
    print("puzzle #1")
else:
    print("puzzle #2")
# across():
print("Across")
for i in range(0,r):
    if (("*" not in lr2[i][0]) and (ls1[i][0] != [])):
        print(ls1[i][0],end="")
        print(b,"",end="")
    for j in range(0,c):
        if "*" in lr2[i][j] :
            if( "*" not in lr2[i][0] and "*" not in lr2[i][c-1] ):
               print()
            elif ( "*" in lr2[r-1][j]):
               print()
            continue    
        else :
            if("*" in lr2[i][j-1]):
               print(ls1[i][j],end="")
               print(b,"",end="")
            print (lr2[i][j],end="" )
    if(r!=c):    
       print()
print()

# down():
print("Down")
for j in range(0,c):
    if (("*" not in lr2[0][j]) and (ls1[0][j] != []) ):
        if(r==c and j!=0):
            print(ls1[0][j],end="")
            print(b,"",end="")
        elif(r != c ):
             print(ls1[0][j],end="")
             print(b,"",end="")

    for i in range(0,r):
       if "*" in lr2[i][j] :
            if("*"  not in lr2[0][j] and "*" not in lr2[r-1][j]) :
                print()
            continue
       else :
           if("*" in lr2[i-1][j]) :
               if( ls1[i][j] == [] ):
                   continue
               else:
                   print(ls1[i][j],end="")
                   print(b,"",end="")
           print(lr2[i][j],end="")
    print()
print()
