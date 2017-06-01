a,b,c,l=input("text:"),input("key:"),0,[]
for x in a:
    if(c==len(b)):
        c=0
        l.append(chr((((ord(x)-97)+(ord(b[c])-97))%26)+97))
        c+=1
    else:
        l.append(chr((((ord(x)-97)+(ord(b[c])-97))%26)+97))
        c+=1
print("".join(l))
