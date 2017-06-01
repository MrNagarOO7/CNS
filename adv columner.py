pt,key,key1,ct,last=input("plaintext:"),input("key1:").split(),input("key2:").split(),[],[]
l,l1,c=[[0 for y in range(1)]for x in range(int(max(key)))],[[0 for y in range(1)]for x in range(int(max(key)))],0
for x in range(len(key)):
    if(len(pt)%len(key)!=0):
        pt=pt+("x") 
for x in pt:
    if(c==len(key)):
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
ct1="".join(ct)
print("inter:",ct1)
c=0
for x in ct1:
    if(c==len(key)):
        c=0
        l1[c].append(x)
        c+=1
    else:
        l1[c].append(x)
        c+=1
for x in range(len(l)):
    l1[x]=l1[x][1:]
    print(l1[x])
for y in key1:
    last.append("".join(l1[int(y)-1]))
print("last:","".join(last))
