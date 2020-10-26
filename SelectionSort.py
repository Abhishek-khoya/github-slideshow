import array as arr
x=arr.array('i')
e=0
while e<=9:
    x.append(int(input("Enter a number : ")))
    e=e+1
e=0
while e<=8:
    m=e
    f=e+1
    while f<=9:
        if x[f]<x[m]: m=f
        f=f+1
    g=x[e]
    x[e]=x[m]
    x[m]=g
    e=e+1
e=0
while e<=9:
    print(x[e])
    e=e+1
