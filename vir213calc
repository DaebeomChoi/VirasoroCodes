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
    rankarr=[[[[[0 for r in range(0,t+1)] for i in range(0,t+1)] for j in range(0,t+1)] for q in range(0,t+1)] for w in range(0,t+1)]
    rankarr[2][0][0][0][0]=1
    rankarr[0][2][0][0][0]=1
    rankarr[0][0][2][0][0]=1
    rankarr[0][0][0][2][0]=1
    rankarr[0][0][0][0][2]=1

    for s in range(3,t+1):
        for n in range(0,s+1):
            for m in range(0,s-n+1):
                for k in range(0,s-n-m+1):
                    for l in range(0,s-n-m-k+1):
                        r=s-n-m-k-l
                        if(n>1):
                            rankarr[n][m][k][l][r]=rankarr[n-2][m][k][l][r]+rankarr[n-2][m+1][k][l][r]
                        elif(n==1):
                            if(m>0):
                                rankarr[n][m][k][l][r]=rankarr[n][m-1][k][l][r]+rankarr[n-1][m-1][k+1][l][r]
                            elif(k>0):
                                rankarr[n][m][k][l][r]=rankarr[n-1][m+1][k-1][l][r]+rankarr[n-1][m][k-1][l+1][r]
                            elif(l>0):
                                rankarr[n][m][k][l][r]=rankarr[n-1][m][k][l-1][r+1]+rankarr[n-1][m][k+1][l-1][r]
                            else:
                                rankarr[n][m][k][l][r]=rankarr[n-1][m][k][l][r]+rankarr[n-1][m][k][l+1][r-1]
                        elif(m>1):
                            rankarr[n][m][k][l][r]=rankarr[n][m-2][k][l][r]+rankarr[n][m-1][k][l][r]+rankarr[n][m-2][k][l+1][r]
                        elif(m==1):
                            if(k>0):
                                rankarr[n][m][k][l][r]=rankarr[n+1][m-1][k-1][l][r]+rankarr[n][m-1][k][l][r]+rankarr[n][m-1][k-1][l][r+1]
                            elif(l>0):
                                rankarr[n][m][k][l][r]=rankarr[n][m][k][l-1][r]+rankarr[n][m-1][k][l][r]+rankarr[n][m-1][k][l-1][r+1]
                            else:
                                rankarr[n][m][k][l][r]=rankarr[n][m-1][k+1][l][r-1]+rankarr[n][m-1][k][l+1][r-1]+rankarr[n][m-1][k][l][r]
                        elif(k>1):
                            rankarr[n][m][k][l][r]=rankarr[n][m][k-2][l][r]+rankarr[n][m+1][k-2][l][r]+rankarr[n][m][k-2][l+1][r]+rankarr[n][m][k-2][l][r+1]
                        elif(k==1):
                            if(l>0):
                                rankarr[n][m][k][l][r]=rankarr[n+1][m][k-1][l-1][r]+rankarr[n][m][k][l-1][r]+rankarr[n][m][k-1][l][r]+rankarr[n][m][k-1][l-1][r+1]
                            else:
                                rankarr[n][m][k][l][r]=rankarr[n][m+1][k-1][l][r-1]+rankarr[n][m][k][l][r-1]+rankarr[n][m][k-1][l+1][r-1]+rankarr[n][m][k-1][l][r]
                        elif(l>1):
                            rankarr[n][m][k][l][r]=rankarr[n][m][k][l-2][r]+rankarr[n][m+1][k][l-2][r]+rankarr[n][m][k+1][l-2][r]+rankarr[n][m][k][l-1][r]+rankarr[n][m][k][l-2][r+1]
                        else:
                            rankarr[n][m][k][l][r]=rankarr[n][m][k][l][r-2]+rankarr[n+1][m][k][l][r-2]+rankarr[n][m+1][k][l][r-2]+rankarr[n][m][k+1][l][r-2]+rankarr[n][m][k][l+1][r-2]+rankarr[n][m][k][l][r-1]
    return rankarr

a11=-1.77091
a12=-1.13613
a13=-0.241073
a14=0.70921
a15=1.49702
a16=1.94188

a21=2.13613
a22=0.29079
a23=-0.941884
a24=-0.497021
a25=1.24107
a26=2.77091

a31=-2.01199
a32=0.805754
a33=0.468136
a34=-1.0617
a35=0.360892
a36=3.43891

a41=1.42692
a42=-1.20623
a43=0.829028
a44=-0.255948
a45=-0.70081
a46=3.90704

a51=-0.514964
a52=0.564681
a53=-0.667993
a54=0.880181
a55=-1.41002
a56=4.14811

c1=-1.94188
c2=1.77091
c3=-1.49702
c4=1.13613
c5=-0.70921
c6=0.241073

d1=-0.0342202
d2=0.11768
d3=-0.20255
d4=0.23677
d5=-0.190779
d6=0.0730987

def rankapp(n,m,k,l,r):
    return c1*d1*(a11**n)*(a21**m)*(a31**k)*(a41**l)*(a51**r)+c2*d2*(a12**n)*(a22**m)*(a32**k)*(a42**l)*(a52**r)+c3*d3*(a13**n)*(a23**m)*(a33**k)*(a43**l)*(a53**r)+c4*d4*(a14**n)*(a24**m)*(a34**k)*(a44**l)*(a54**r)+c5*d5*(a15**n)*(a25**m)*(a35**k)*(a45**l)*(a55**r)+c6*d6*(a16**n)*(a26**m)*(a36**k)*(a46**l)*(a56**r)

t=15
rk=rank(t)

excep=[]
neg=[]
value=[]
for n in range(14,16):
    for i in range(0,n+1):
        for j in range(0,n+1-i):
            for k in range(0,n+1-i-j):
                for l in range(0,n+1-i-j-k):
                    for a in range(0,i+1):
                        for b in range(0,j+1):
                            for c in range(0,k+1):
                                for d in range(0,l+1):
                                    for e in range(max(0,2-a-b-c-d), min(n-i-j-k-l, n-2-a-b-c-d)+1):
                                        f=a+b+c+d+e
                                        m=n-i-j-k-l
                                        coeff=(n-1)*(n-2)*(5*rk[a+1][b][c][d][e]*rk[i-a+1][j-b][k-c][l-d][m-e]+9*rk[a][b+1][c][d][e]*rk[i-a][j-b+1][k-c][l-d][m-e]+12*rk[a][b][c+1][d][e]*rk[i-a][j-b][k-c+1][l-d][m-e]+14*rk[a][b][c][d+1][e]*rk[i-a][j-b][k-c][l-d+1][m-e]+15*rk[a][b][c][d][e+1]*rk[i-a][j-b][k-c][l-d][m-e+1])
                                        psi=rk[i][j][k][l][m]*((n-f)*(n-f-1)*(5*a+9*b+12*c+14*d+15*e)+f*(f-1)*(5*(i-a)+9*(j-b)+12*(k-c)+14*(l-d)+15*(m-e)))
                                        if(coeff>psi):
                                            neg.append([n,i,j,k,l,m,a,b,c,d,e])
                                        if(coeff==psi):
                                            excep.append([n,i,j,k,l,m,a,b,c,d,e])
                                        print([n,i])
print(excep)
print(neg)
