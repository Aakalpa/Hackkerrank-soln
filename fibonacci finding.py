mod = 1000000007
M = [[1,1],[1,0]]
def fastexp(m,n):
    if n <=1 : 
        return m
    x = matmul(m,m)
    temp = fastexp(x,n//2)
    if n&1:
        temp = matmul(temp,m) 
    return temp    
def matmul(a,b):
    w = (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod
    x = (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod
    y = (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod
    z = (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod
    return [[w,x],[y,z]]
for _ in range(int(input())):
    a,b,n = map(int,input().split())
    t = fastexp(M,n)
    print( (t[1][0]*b + t[1][1]*a) % mod )
