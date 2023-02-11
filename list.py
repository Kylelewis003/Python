n = input()
lst = list(n)
print(lst)
lst.sort()
temp = 0
for i in lst:
    count = 0
    for j in lst :
        if i == j:
            count+=1
        else:
            break
    print("The number of occurances of ", i ," is : " ,count)
    i+=count    
            
    
