import array as arr
a=arr.array('i')
req=int(input("How many numbers do you wants to sort ? "))
x=range(req)
for i in x:a.append(int(input("Enter a number : ")))
y=range(req-1,0,-1)
for j in y:
    z=range(j)
    for k in z:
        if a[k]>a[k+1]:a[k],a[k+1]=a[k+1],a[k]
for m in a:print(m)
    