pt,key,ct=input("plaintext:"),input("key:").split(),[]
l,c=[[0 for y in range(1)]for x in range(int(max(key)))],0
for x in range(len(key)):
    if(len(pt)%len(key)!=0):
        pt=pt+("x") 
for x in pt:
    if(c==len(l)):
        c=0
        l[c].append(x)
        c+=1
    else:
        l[c].append(x)
        c+=1
for x in range(len(l)):
    l[x]=l[x][1:]
for y in key:
    ct.append("".join(l[int(y)-1]))
print("".join(ct))
