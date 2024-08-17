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

#intersection with F-curves

t=12
rk=rank(t)

for n in range(8,t+1):
    for i in range(0,n+1):
        for j in range(0,n+1-i):
            for k in range(0,n+1-i-j):
                for l in range(0,n+1-i-j-k):
                    m=n-i-j-k-l
                    if(rk[i][j][k][l][m]<2):
                        break
                    for f11 in range(0,i+1):
                        for f21 in range(0,i+1-f11):
                            for f31 in range(0,i+1-f11-f21):
                                f41=i-f11-f21-f31
                                for f12 in range(0,j+1):
                                    for f22 in range(0,j+1-f12):
                                        for f32 in range(0,j+1-f12-f22):
                                            f42=j-f12-f22-f32
                                            for f13 in range(0,k+1):
                                                for f23 in range(0,k+1-f13):
                                                    for f33 in range(0,k+1-f13-f23):
                                                        f43=k-f13-f23-f33
                                                        for f14 in range(0,l+1):
                                                            for f24 in range(0,l+1-f14):
                                                                for f34 in range(0,l+1-f14-f24):
                                                                    f44=l-f14-f24-f34
                                                                    for f15 in range(max(0,1-f11-f12-f13-f14),m+1):
                                                                        for f25 in range(max(0,1-f21-f22-f23-f24),m+1-f15):
                                                                            for f35 in range(max(0,1-f31-f32-f33-f34),m+1-f15-f25):
                                                                                f45=m-f15-f25-f35
                                                                                if(f41+f42+f43+f44+f45==0):
                                                                                    break
                                                                                

                                                                                



