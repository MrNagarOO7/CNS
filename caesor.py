pt,key,ct=input("plain text:"),int(input("key:")),[]
for x in pt:
    ct.append(chr((((ord(x)-97)+key)%26)+97))
print("".join(ct))
