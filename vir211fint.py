import itertools

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

t=20
rk=rank(t)
nonample=[]

for n in range(15,18):
    for i in range(0,n+1):
        for j in range(0,n+1-i):
            for k in range(0,n+1-i-j):
                l=n-i-j-k
                if(rk[i][j][k][l]<2):
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
                                                    for f14 in range(max(0,1-f11-f12-f13),l+1):
                                                        for f24 in range(max(0,1-f21-f22-f23),l+1-f14):
                                                            for f34 in range(max(0,1-f31-f32-f33),l+1-f14-f24):
                                                                f44=l-f14-f24-f34
                                                                if(f41+f42+f43+f44==0):
                                                                    break
                                                                list1=[]
                                                                list2=[]
                                                                list3=[]
                                                                list4=[]
                                                                if(rk[f11+1][f12][f13][f14]>0):
                                                                    list1.append(1)
                                                                if(rk[f11][f12+1][f13][f14]>0):
                                                                    list1.append(2)
                                                                if(rk[f11][f12][f13+1][f14]>0):
                                                                    list1.append(3)
                                                                if(rk[f11][f12][f13][f14+1]>0):
                                                                    list1.append(4)
                                                                if(rk[f21+1][f22][f23][f24]>0):
                                                                    list2.append(1)
                                                                if(rk[f21][f22+1][f23][f24]>0):
                                                                    list2.append(2)
                                                                if(rk[f21][f22][f23+1][f24]>0):
                                                                    list2.append(3)
                                                                if(rk[f21][f22][f23][f24+1]>0):
                                                                    list2.append(4)
                                                                if(rk[f31+1][f32][f33][f34]>0):
                                                                    list3.append(1)
                                                                if(rk[f31][f32+1][f33][f34]>0):
                                                                    list3.append(2)
                                                                if(rk[f31][f32][f33+1][f34]>0):
                                                                    list3.append(3)
                                                                if(rk[f31][f32][f33][f34+1]>0):
                                                                    list3.append(4)
                                                                if(rk[f41+1][f42][f43][f44]>0):
                                                                    list4.append(1)
                                                                if(rk[f41][f42+1][f43][f44]>0):
                                                                    list4.append(2)
                                                                if(rk[f41][f42][f43+1][f44]>0):
                                                                    list4.append(3)
                                                                if(rk[f41][f42][f43][f44+1]>0):
                                                                    list4.append(4)
                                                                mlist=list(itertools.product(list1,list2,list3,list4))
                                                                check=0
                                                                for pair in mlist:
                                                                    a=pair.count(1)
                                                                    b=pair.count(2)
                                                                    c=pair.count(3)
                                                                    d=pair.count(4)
                                                                    if(rk[a][b][c][d]>1):
                                                                        check=1
                                                                        break
                                                                if(check==0):
                                                                    nonample.append([n,i,j,k,l,f11,f12,f13,f14,f21,f22,f23,f24,f31,f32,f33,f34,f41,f42,f43,f44])
                                                                    print([n,i,j,k,l,f11,f12,f13,f14,f21,f22,f23,f24,f31,f32,f33,f34,f41,f42,f43,f44])
        print(i)
print(nonample)


                                                                

