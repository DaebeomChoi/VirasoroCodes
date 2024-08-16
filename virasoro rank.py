def fusion(p,q,r1,s1,r2,s2):
    tensor=[]
    for r3 in range(abs(r2-r1)+1, min(r2+r1, 2*p-r1-r2), 2):
        for s3 in range(abs(s2-s1)+1, s1+s2, 2):
            if (s3>q/2):
                s3=q-s3
            tensor.append([r3,s3])
    return tensor

def fusdim(p,q,r1,s1,r2,s2,r3,s3):
    count=0
    if(abs(r2-r1)+1<=r3 and r3<min(r2+r1, 2*p-r1-r2) and (r2+r1-r3)%2==1 and abs(s2-s1)+1<=s3 and s3<min(s2+s1, 2*q-s1-s2) and (s2+s1-s3)%2==1):
        count=count+1
    r3=p-r3
    s3=q-s3
    if(abs(r2-r1)+1<=r3 and r3<min(r2+r1, 2*p-r1-r2) and (r2+r1-r3)%2==1 and abs(s2-s1)+1<=s3 and s3<min(s2+s1, 2*q-s1-s2) and (s2+s1-s3)%2==1):
        count=count+1
    return count

def rank(t):
    rankarr=[[[[0 for i in range(0,t+1)] for j in range(0,t+1)] for q in range(0,t+1)] for w in range(0,t+1)]
    rankarr[2][0][0][0]=1
    rankarr[0][2][0][0]=1
    rankarr[0][0][2][0]=1
    rankarr[0][0][0][2]=1

    for s in range(3,t+1):
        for n in range(0,s+1):
            for m in range(0,s-n+1):
                for k in range(0,s-n-m+1):
                    l=s-n-m-k
                    if(n>1):
                        rankarr[n][m][k][l]=rankarr[n-2][m][k][l]+rankarr[n-2][m+1][k][l]
                    elif(n==1):
                        if(m>0):
                            rankarr[n][m][k][l]=rankarr[n][m-1][k][l]+rankarr[n-1][m-1][k+1][l]
                        elif(k>0):
                            rankarr[n][m][k][l]=rankarr[n-1][m+1][k-1][l]+rankarr[n-1][m][k-1][l+1]
                        else:
                            rankarr[n][m][k][l]=rankarr[n-1][m][k][l]+rankarr[n-1][m][k+1][l-1]
                    elif(m>1):
                        rankarr[n][m][k][l]=rankarr[n][m-2][k][l]+rankarr[n][m-1][k][l]+rankarr[n][m-2][k][l+1]
                    elif(m==1):
                        if(k>0):
                            rankarr[n][m][k][l]=rankarr[n+1][m-1][k-1][l]+rankarr[n][m-1][k][l]+rankarr[n][m-1][k-1][l+1]
                        if(l>0):
                            rankarr[n][m][k][l]=rankarr[n][m-1][k+1][l-1]+rankarr[n][m-1][k][l]+rankarr[n][m][k][l-1]
                    elif(k>1):
                        rankarr[n][m][k][l]=rankarr[n][m][k-2][l]+rankarr[n][m+1][k-2][l]+rankarr[n][m][k-2][l+1]+rankarr[n][m][k-1][l]
                    elif(k==1):
                        rankarr[n][m][k][l]=rankarr[n+1][m][k-1][l-1]+rankarr[n][m+1][k-1][l-1]+rankarr[n][m][k-1][l]+rankarr[n][m][k][l-1]
                    else:
                        rankarr[n][m][k][l]=rankarr[n+1][m][k][l-2]+rankarr[n][m+1][k][l-2]+rankarr[n][m][k+1][l-2]+rankarr[n][m][k][l-1]+rankarr[n][m][k][l-2]

    return rankarr

       
t=15

#calculatingallW2
rk=rank(t)
list1=[]
list2=[]
for i in range(2,2):
    coeff=(4*rk[i+1][0][0][0]*rk[t-i+1][0][0][0]+7*rk[i][1][0][0]*rk[t-i][1][0][0]+9*rk[i][0][1][0]*rk[t-i][0][1][0]+10*rk[i][0][0][1]*rk[t-i][0][0][1])/(4*rk[t][0][0][0])
    if(coeff<2):
        list1.append(i)
    if(coeff<2.0364 or coeff>2.0384):
        list2.append(i)
    print(coeff)
print(list1)
print(list2)
res=0

list=[]


#all the coefficients
best=0
for n in range(10,10):
    for i in range(0,n+1):
        for j in range(0,n+1-i):
            for k in range(0,n+1-i-j):
                for a in range(0,i+1):
                    for b in range(0,j+1):
                        for c in range(0,k+1):
                            for d in range(max(0,2-a-b-c), min(n-i-j-k, n-2-a-b-c)+1):
                                if(a+b+c+d==3):
                                    m=n-i-j-k-d
                                    coeff=(4*rk[a+1][b][c][d]*rk[i-a+1][j-b][k-c][m]+7*rk[a][b+1][c][d]*rk[i-a][j-b+1][k-c][m]+9*rk[a][b][c+1][d]*rk[i-a][j-b][k-c+1][m]+10*rk[a][b][c][d+1]*rk[i-a][j-b][k-c][m+1])/(4*rk[i][j][k][n-i-j-k])
                                    best=max(coeff,best)
                                    print(coeff)
print(best)

#coefficient of delta_i
pt=3
num=0
for n in range(10,10):
    for i in range(0,n-pt+1):
        for j in range(0,n-pt+1-i):
            for k in range(0,n-pt+1-i-j):
                for a in range(0,pt+1):
                    for b in range(0,pt+1-a):
                        for c in range(0,pt+1-a-b):
                            d=pt-a-b-c
                            l=n-pt-i-j-k
                            coeff=(4*rk[a+1][b][c][d]*rk[i+1][j][k][l]+7*rk[a][b+1][c][d]*rk[i][j+1][k][l]+9*rk[a][b][c+1][d]*rk[i][j][k+1][l]+10*rk[a][b][c][d+1]*rk[i][j][k][l+1])/(4*rk[i+a][j+b][k+c][l+d])
                            print(coeff)
                            num=max(coeff,num)

print(num)

big=0

list3=[]

#coefficient of delta_i for special choice of modules
for n in range(8,8):
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            for k in range(0,n-1-i-j):
                l=n-2-i-j-k
                coeff=(4*rk[3][0][0][0]*rk[i+1][j][k][l]+7*rk[2][1][0][0]*rk[i][j+1][k][l]+9*rk[2][0][1][0]*rk[i][j][k+1][l]+10*rk[2][0][0][1]*rk[i][j][k][l+1])/(4*rk[i+2][j][k][l])
                print(coeff)
                big=max(big,coeff)
                if(coeff==1.75):
                    list3.append([n,i,j,k])

print(list3)
print(big)

#checking effectivity of delta_i
pt=3
list4=[]
for n in range(8,8):
    for i in range(0,n-pt+1):
        for j in range(0,n-pt+1-i):
            for k in range(0,n-pt+1-i-j):
                for a in range(0,pt+1):
                    for b in range(0,pt+1-a):
                        for c in range(0,pt+1-a-b):
                            d=pt-a-b-c
                            l=n-pt-i-j-k
                            coeff=(4*rk[a+1][b][c][d]*rk[i+1][j][k][l]+7*rk[a][b+1][c][d]*rk[i][j+1][k][l]+9*rk[a][b][c+1][d]*rk[i][j][k+1][l]+10*rk[a][b][c][d+1]*rk[i][j][k][l+1])/(4*rk[i+a][j+b][k+c][l+d])

#checking effectivity of everything
excep=[]
for n in range(8,t+1):
    for i in range(0,n+1):
        for j in range(0,n+1-i):
            for k in range(0,n+1-i-j):
                for a in range(0,i+1):
                    for b in range(0,j+1):
                        for c in range(0,k+1):
                            for d in range(max(0,2-a-b-c), min(n-i-j-k, n-2-a-b-c)+1):
                                e=a+b+c+d
                                m=n-i-j-k-d
                                coeff=(n-1)*(n-2)*(4*rk[a+1][b][c][d]*rk[i-a+1][j-b][k-c][m]+7*rk[a][b+1][c][d]*rk[i-a][j-b+1][k-c][m]+9*rk[a][b][c+1][d]*rk[i-a][j-b][k-c+1][m]+10*rk[a][b][c][d+1]*rk[i-a][j-b][k-c][m+1])
                                psi=rk[i][j][k][n-i-j-k]*((n-e)*(n-e-1)*(4*a+7*b+9*c+10*d)+e*(e-1)*(4*(i-a)+7*(j-b)+9*(k-c)+10*m))
                                if(psi<=coeff):
                                    excep.append([n,i,j,k,a,b,c,d])
                                print([n,i])
print(excep)