def rank(t):
    rankarr=[[[[[[0 for a in range(0,t+1)] for r in range(0,t+1)] for i in range(0,t+1)] for j in range(0,t+1)] for q in range(0,t+1)] for w in range(0,t+1)]
    rankarr[2][0][0][0][0][0]=1
    rankarr[0][2][0][0][0][0]=1
    rankarr[0][0][2][0][0][0]=1
    rankarr[0][0][0][2][0][0]=1
    rankarr[0][0][0][0][2][0]=1
    rankarr[0][0][0][0][0][2]=1

    for s in range(3,t+1):
        for n in range(0,s+1):
            for m in range(0,s-n+1):
                for k in range(0,s-n-m+1):
                    for l in range(0,s-n-m-k+1):
                        for p in range(0, s-n-m-k-l+1):
                            r=s-n-m-k-l-p
                            if(n>1):
                                rankarr[n][m][k][l][r][p]=rankarr[n-2][m][k][l][r][p]+rankarr[n-2][m+1][k][l][r][p]
                            elif(n==1):
                                if(m>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n][m-1][k][l][r][p]+rankarr[n-1][m-1][k+1][l][r][p]
                                elif(k>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n-1][m+1][k-1][l][r][p]+rankarr[n-1][m][k-1][l+1][r][p]
                                elif(l>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n-1][m][k][l-1][r+1][p]+rankarr[n-1][m][k+1][l-1][r][p]
                                elif(r>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n-1][m][k][l][r-1][p+1]+rankarr[n-1][m][k][l+1][r-1][p]
                                else:
                                    rankarr[n][m][k][l][r][p]=rankarr[n-1][m][k][l][r+1][p-1]+rankarr[n-1][m][k][l][r][p]
                            elif(m>1):
                                rankarr[n][m][k][l][r][p]=rankarr[n][m-2][k][l][r][p]+rankarr[n][m-1][k][l][r][p]+rankarr[n][m-2][k][l+1][r][p]
                            elif(m==1):
                                if(k>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n+1][m-1][k-1][l][r][p]+rankarr[n][m-1][k][l][r][p]+rankarr[n][m-1][k-1][l][r+1][p]
                                elif(l>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n][m][k][l-1][r][p]+rankarr[n][m-1][k][l][r][p]+rankarr[n][m-1][k][l-1][r][p+1]
                                elif(r>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n][m-1][k+1][l][r-1][p]+rankarr[n][m-1][k][l][r][p]+rankarr[n][m-1][k][l][r-1][p+1]
                                else:
                                    rankarr[n][m][k][l][r][p]=rankarr[n][m-1][k][l+1][r][p-1]+rankarr[n][m-1][k][l][r+1][p-1]+rankarr[n][m-1][k][l][r][p]
                            elif(k>1):
                                rankarr[n][m][k][l][r][p]=rankarr[n][m][k-2][l][r][p]+rankarr[n][m+1][k-2][l][r][p]+rankarr[n][m][k-2][l+1][r][p]+rankarr[n][m][k-2][l][r][p+1]
                            elif(k==1):
                                if(l>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n+1][m][k-1][l-1][r][p]+rankarr[n][m][k][l-1][r][p]+rankarr[n][m][k-1][l-1][r+1][p]+rankarr[n][m][k-1][l-1][r][p+1]
                                elif(r>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n][m+1][k-1][l][r-1][p]+rankarr[n][m][k-1][l+1][r-1][p]+rankarr[n][m][k-1][l][r][p]+rankarr[n][m][k-1][l][r-1][p+1]
                                else:
                                    rankarr[n][m][k][l][r][p]=rankarr[n][m][k-1][l][r][p]+rankarr[n][m][k][l][r][p-1]+rankarr[n][m][k-1][l+1][r][p-1]+rankarr[n][m][k-1][l][r+1][p-1]
                            elif(l>1):
                                rankarr[n][m][k][l][r][p]=rankarr[n][m][k][l-2][r][p]+rankarr[n][m+1][k][l-2][r][p]+rankarr[n][m][k][l-1][r][p]+rankarr[n][m][k][l-2][r+1][p]+rankarr[n][m][k][l-2][r][p+1]
                            elif(l==1):
                                if(r>0):
                                    rankarr[n][m][k][l][r][p]=rankarr[n+1][m][k][l-1][r-1][p]+rankarr[n][m][k+1][l-1][r-1][p]+rankarr[n][m][k][l][r-1][p]+rankarr[n][m][k][l-1][r][p]+rankarr[n][m][k][l-1][r-1][p+1]
                                else:
                                    rankarr[n][m][k][l][r][p]=rankarr[n][m+1][k][l-1][r][p-1]+rankarr[n][m][k+1][l-1][r][p-1]+rankarr[n][m][k][l][r][p-1]+rankarr[n][m][k][l-1][r+1][p-1]+rankarr[n][m][k][l-1][r][p]
                            elif(r>1):
                                rankarr[n][m][k][l][r][p]=rankarr[n][m][k][l][r-2][p]+rankarr[n][m+1][k][l][r-2][p]+rankarr[n][m][k+1][l][r-2][p]+rankarr[n][m][k][l+1][r-2][p]+rankarr[n][m][k][l][r-1][p]+rankarr[n][m][k][l][r-2][p+1]
                            else:
                                rankarr[n][m][k][l][r][p]=rankarr[n][m][k][l][r][p-2]+rankarr[n][m+1][k][l][r][p-2]+rankarr[n][m][k+1][l][r][p-2]+rankarr[n][m][k][l+1][r][p-2]+rankarr[n][m][k][l][r+1][p-2]+rankarr[n][m][k][l][r][p-1]+rankarr[n+1][m][k][l][r][p-2]
    return rankarr

t=20
rk=rank(t)

neg=[]
excep=[]

for n in range(15,16):
    for i in range(0,n+1):
        for j in range(0,n+1-i):
            for k in range(0,n+1-i-j):
                for l in range(0,n+1-i-j-k):
                    for r in range(0,n+1-i-j-k-l):
                        if (rk[i][j][k][l][r][n-i-j-k-l-r]<2):
                            break
                        for a in range(0,i+1):
                            for b in range(0,j+1):
                                for c in range(0,k+1):
                                    for d in range(0,l+1):
                                        for e in range(0,r+1):
                                            for f in range(max(0,2-a-b-c-d-e), min(n-i-j-k-l-r, n-2-a-b-c-d-e)+1):
                                                g=a+b+c+d+e+f
                                                m=n-i-j-k-l-r
                                                coeff=(n-1)*(n-2)*(6*rk[a+1][b][c][d][e][f]*rk[i-a+1][j-b][k-c][l-d][r-e][m-f]+11*rk[a][b+1][c][d][e][f]*rk[i-a][j-b+1][k-c][l-d][r-e][m-f]+15*rk[a][b][c+1][d][e][f]*rk[i-a][j-b][k-c+1][l-d][r-e][m-f]+18*rk[a][b][c][d+1][e][f]*rk[i-a][j-b][k-c][l-d+1][r-e][m-f]+20*rk[a][b][c][d][e+1][f]*rk[i-a][j-b][k-c][l-d][r-e+1][m-f]+21*rk[a][b][c][d][e][f+1]*rk[i-a][j-b][k-c][l-d][r-e][m-f+1])
                                                psi=rk[i][j][k][l][r][m]*((n-g)*(n-g-1)*(6*a+11*b+15*c+18*d+20*e+21*f)+g*(g-1)*(6*(i-a)+11*(j-b)+15*(k-c)+18*(l-d)+20*(r-e)+21*(m-f)))
                                                if(coeff>psi):
                                                    neg.append([n,i,j,k,l,m,a,b,c,d,e])
                                                if(coeff==psi):
                                                    excep.append([n,i,j,k,l,r,m,a,b,c,d,e,f])
                                                print([n,i])

print(neg)
print(excep)