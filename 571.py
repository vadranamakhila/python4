m,n=map(int,raw_input().split())
list=[int(i) for i in raw_input().split()]
if m in list:
    count=list.count(m)
    print count
elif n in list:
    count=list.count(n)
    print count
else:
    print (0)
