X="Do not cry me a river"
X=X.split(' ')
X.reverse()
M=X[:]
print(X)
print(M)
n=0
L=[]
while 1==1:
    zwy=X[n]
    listen=list(zwy)
    listen.reverse()
    cjj="".join(listen)
    L.append(cjj)
    n=n+1
    if n>len(X)-1:
        break
L.sort()
L.reverse()
print(L)