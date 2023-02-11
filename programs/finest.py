n = int(input(""))
lst = []
for i in range(0,n):
    l = int(input(""))
    lst.append(l)
    
lst1 = []

for i in lst :
    for t in range (0,10):
        f = (t**3)+((t+1)**3)
        if(i == f):
            lst1.append(i)
        
lst1.sort()

if(lst1):
    for i in lst1 :
        print(i,end = " ")
else:
    print(-1)

        
    
            
    
    

    