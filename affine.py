pt,ct=list(input("plain text:").lower()),[] # f(X)=3X+2 compare f(X)=AX+B  A=3,B=2=Keys
[ct.append(chr((((3*(ord(x)-97))+2)%26)+97)) for x in pt ]
print(ct)
