a,ct,f=int(input("key:")),[],1
b,l,count=input("p.t:"),[[0 for x in range(1)] for y in range(a)],0
for x in b:
    if(x==" "):
        x="x"
    if(f==1):
        if(count==a-1):
            f=2
            l[count].append(x)
            count-=1
        else:
            l[count].append(x)
            count+=1
    else:
        if(count==0):
            f=1
            l[count].append(x)
            count+=1
        else:
            l[count].append(x)
            count-=1
for x in range(a):
    l[x]=l[x][1:]
for x in range(a):
    a="".join(l[x])
    ct.append(a)
print("".join(ct))

