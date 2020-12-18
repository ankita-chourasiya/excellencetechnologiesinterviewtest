def dict(A):
    data=A.values()
    value=max(data)
              
    res = {}
    for key in A.keys():
        if A.get(key)==value:
            res[key] = value
    print(res)   

d = {"1":"name1",2":"name2","3":"name3"}       
d1={'1':60,'2':50,'3':70}
dict(d1)
