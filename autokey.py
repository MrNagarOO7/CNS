l,ct=[[0 for x in range(26)]for y in range(26)],[]
for x in range(26):
    a=97
    a=a+x
    for y in range(26):
        if(a==123):
            a=97
            l[x][y]=chr(a)
            a+=1
        else:
            l[x][y]=chr(a)
            a+=1
#for x in range(26):
 #   print(l[x])
pt,key=list(input("plain text:").lower()),list(input("key:").lower())
key.extend(pt)
key=key[:len(pt)]#if len(key)!=len(pt) then append pt
                                          #to key until both len equal
for x,y in zip(key,pt):
    ct.append(l[ord(x)-97][ord(y)-97])
print(ct)
    
            
    
