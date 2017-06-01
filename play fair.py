key,pf,count,z,ct=input("small alphabetic key:"),[],0,[[0 for x in range(5)]for y in range(5)],[]
for x in key :
 if(x not in pf):
     if(x=="j"):
         pf.append("i")
     else:
         pf.append(x)
print(pf)
k={chr(x) for x in range(97,123)}
m=list(k-set(pf)-{"j"})
m.sort()
pf.extend(m)
for x in range(5):
    for y in range(5):
            z[x][y]=pf[count]
            count+=1
    print(z[x])
pt=input("enter plaintext:")
pt=list(pt.translate(str.maketrans("j","i")))
for x in range(len(pt)-1):
    if(pt[x]==pt[x+1]):
        pt.insert(x+1,"x")
if(len(pt)%2!=0):
        pt.append("x")
print("plain text:",pt)
for k in range(0,len(pt)-1,2):
    for x in range(5):
      for y in range(5):
         if(pt[k]==z[x][y]):
            r1,c1=x,y
         if(pt[k+1]==z[x][y]):
             r2,c2=x,y
    if(r1==r2):
        c1,c2=c1+1,c2+1
        if(c1>4):c1=0
        if(c2>4):c2=0
        ct.append(z[r1][c1])
        ct.append(z[r2][c2])
    elif(c1==c2):
        r1,r2=r1+1,r2+1
        if(r1>4):r1=0
        if(r2>4):r2=0
        ct.append(z[r1][c1])
        ct.append(z[r2][c2])
    else:
        ct.append(z[r1][c2])
        ct.append(z[r2][c1])
print("Cipher Text:",ct)
