def extdgcd(x,y):
    x1,y1=x,y
    while(y!=0):
        x,y=y,x%y
    gcd=x
    z1=gcd
