max_slices,type_pizza=input("").split()
no_of_slices=[]
a=input("").split()
for x in a:
    if int(x) <= int(max_slices):
        no_of_slices.append(int(x))
        no_of_slices.sort()
    else :
        a=input("Number of slices in each type of pizza < Max Slices:").split()
        continue
ans=0
c=0
f=[]
if sum(no_of_slices)>int(max_slices) :
    for y in range(0,int(type_pizza)) :
        ans+=no_of_slices[c]
        f.append(c)
        if ans > int(max_slices):
            break
        else :
            c=c+1
    c=0
    for y in range(0,int(type_pizza)) :
        if (ans-no_of_slices[c]) > int(max_slices) :
            c=c+1
        else :
            f.remove(c)
            break
    print(len(f))
    print(*f)

else :
    print(len(no_of_slices))
    for x in range(0,len(no_of_slices)) :
        f.append(x)
    print(*f)