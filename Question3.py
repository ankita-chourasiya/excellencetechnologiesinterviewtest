def max(A):
    count=0
    list=[]
    for ch in A:
        if ch==1:
            count=count+1
        elif count>0:
            list.append(count)
            count=0
    list.append(count)
    l=sorted(list)
    print(l[len(l)-1])

list=[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
max(list)
