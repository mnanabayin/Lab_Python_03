# first 50 prime Numbers
i = 1
c=0
for k in range(1,250):
    if c >=50:
        break
    count = 0
    for j in range(1,i+1):
        a=i%j
        if (a==0):
            count+=1
    if (count == 2):
        if c%10==0:
            print '\n',
        print (i),
        c+=1
        
    else:
        k-=1
    i+=1
