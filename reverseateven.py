n=int(input())
i=0
k=1
while i<n:
    j=0
    s1=""
    while j<i+1:
        if i%2==0:
            s1=s1+str(k)+" "
        else:
            m=str(k)
            s1=s1+m[::-1]+" "
        k=k+1
        j=j+1
    if i%2!=0:
        s1=s1[::-1]
        print(s1[1:])
    else:
        print(s1)
        
    i=i+1
    
        
