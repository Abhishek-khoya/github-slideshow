import array as arr
req=int(input("How many numbers do you wants to sort ? : "))
a=arr.array('i')
x=range(req)
for i in x: a.append(int(input("Enter a number : ")))
y=range(req-1)
for e in y:
    z=range(e+1,req)
    for f in z:
        if a[f]<a[e]:
            a[f],a[e]=a[e],a[f]
for j in a: print(j)
