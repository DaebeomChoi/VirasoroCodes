import itertools

def rank5(t):
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

def rank6(t):
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

def rank7(t):
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

t=12
rk5=rank5(t)
rk6=rank6(t)
rk7=rank7(t)

critical=[]
nonnef=[]
nonzero=[]
nonample=[]

for n in range(5,8):
    for i in range(0,n+1):
        for j in range(0,n+1-i):
            for k in range(0,n+1-i-j):
                l=n-i-j-k
                check1=0
                check2=0
                check3=0
                if(i+2*j+3*k+4*l<9 or 18<i+2*j+3*k+4*l):
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
                                                                if(rk5[f11+1][f12][f13][f14]>0):
                                                                    list1.extend([1]*rk5[f11+1][f12][f13][f14])
                                                                if(rk5[f11][f12+1][f13][f14]>0):
                                                                    list1.extend([2]*rk5[f11][f12+1][f13][f14])
                                                                if(rk5[f11][f12][f13+1][f14]>0):
                                                                    list1.extend([3]*rk5[f11][f12][f13+1][f14])
                                                                if(rk5[f11][f12][f13][f14+1]>0):
                                                                    list1.extend([4]*rk5[f11][f12][f13][f14+1])
                                                                if(rk5[f21+1][f22][f23][f24]>0):
                                                                    list2.extend([1]*rk5[f21+1][f22][f23][f24])
                                                                if(rk5[f21][f22+1][f23][f24]>0):
                                                                    list2.extend([2]*rk5[f21][f22+1][f23][f24])
                                                                if(rk5[f21][f22][f23+1][f24]>0):
                                                                    list2.extend([3]*rk5[f21][f22][f23+1][f24])
                                                                if(rk5[f21][f22][f23][f24+1]>0):
                                                                    list2.extend([4]*rk5[f21][f22][f23][f24+1])
                                                                if(rk5[f31+1][f32][f33][f34]>0):
                                                                    list3.extend([1]*rk5[f31+1][f32][f33][f34])
                                                                if(rk5[f31][f32+1][f33][f34]>0):
                                                                    list3.extend([2]*rk5[f31][f32+1][f33][f34])
                                                                if(rk5[f31][f32][f33+1][f34]>0):
                                                                    list3.extend([3]*rk5[f31][f32][f33+1][f34])
                                                                if(rk5[f31][f32][f33][f34+1]>0):
                                                                    list3.extend([4]*rk5[f31][f32][f33][f34+1])
                                                                if(rk5[f41+1][f42][f43][f44]>0):
                                                                    list4.extend([1]*rk5[f41+1][f42][f43][f44])
                                                                if(rk5[f41][f42+1][f43][f44]>0):
                                                                    list4.extend([2]*rk5[f41][f42+1][f43][f44])
                                                                if(rk5[f41][f42][f43+1][f44]>0):
                                                                    list4.extend([3]*rk5[f41][f42][f43+1][f44])
                                                                if(rk5[f41][f42][f43][f44+1]>0):
                                                                    list4.extend([4]*rk5[f41][f42][f43][f44+1])
                                                                mlist=list(itertools.product(list1,list2,list3,list4))
                                                                slist1=[]
                                                                slist2=[]
                                                                slist3=[]
                                                                slist4=[]
                                                                f15=0
                                                                f25=0
                                                                f35=0
                                                                f45=0
                                                                if(rk6[f11+1][f12][f13][f14][f15]>0):
                                                                    slist1.extend([1]*rk6[f11+1][f12][f13][f14][f15])
                                                                if(rk6[f11][f12+1][f13][f14][f15]>0):
                                                                    slist1.extend([2]*rk6[f11][f12+1][f13][f14][f15])
                                                                if(rk6[f11][f12][f13+1][f14][f15]>0):
                                                                    slist1.extend([3]*rk6[f11][f12][f13+1][f14][f15])
                                                                if(rk6[f11][f12][f13][f14+1][f15]>0):
                                                                    slist1.extend([4]*rk6[f11][f12][f13][f14+1][f15])
                                                                if(rk6[f11][f12][f13][f14][f15+1]>0):
                                                                    slist1.extend([5]*rk6[f11][f12][f13][f14][f15+1])
                                                                if(rk6[f21+1][f22][f23][f24][f25]>0):
                                                                    slist2.extend([1]*rk6[f21+1][f22][f23][f24][f25])
                                                                if(rk6[f21][f22+1][f23][f24][f25]>0):
                                                                    slist2.extend([2]*rk6[f21][f22+1][f23][f24][f25])
                                                                if(rk6[f21][f22][f23+1][f24][f25]>0):
                                                                    slist2.extend([3]*rk6[f21][f22][f23+1][f24][f25])
                                                                if(rk6[f21][f22][f23][f24+1][f25]>0):
                                                                    slist2.extend([4]*rk6[f21][f22][f23][f24+1][f25])
                                                                if(rk6[f21][f22][f23][f24][f25+1]>0):
                                                                    slist2.extend([5]*rk6[f21][f22][f23][f24][f25+1])
                                                                if(rk6[f31+1][f32][f33][f34][f35]>0):
                                                                    slist3.extend([1]*rk6[f31+1][f32][f33][f34][f35])
                                                                if(rk6[f31][f32+1][f33][f34][f35]>0):
                                                                    slist3.extend([2]*rk6[f31][f32+1][f33][f34][f35])
                                                                if(rk6[f31][f32][f33+1][f34][f35]>0):
                                                                    slist3.extend([3]*rk6[f31][f32][f33+1][f34][f35])
                                                                if(rk6[f31][f32][f33][f34+1][f35]>0):
                                                                    slist3.extend([4]*rk6[f31][f32][f33][f34+1][f35])
                                                                if(rk6[f31][f32][f33][f34][f35+1]>0):
                                                                    slist3.extend([5]*rk6[f31][f32][f33][f34][f35+1])
                                                                if(rk6[f41+1][f42][f43][f44][f45]>0):
                                                                    slist4.extend([1]*rk6[f41+1][f42][f43][f44][f45])
                                                                if(rk6[f41][f42+1][f43][f44][f45]>0):
                                                                    slist4.extend([2]*rk6[f41][f42+1][f43][f44][f45])
                                                                if(rk6[f41][f42][f43+1][f44][f45]>0):
                                                                    slist4.extend([3]*rk6[f41][f42][f43+1][f44][f45])
                                                                if(rk6[f41][f42][f43][f44+1][f45]>0):
                                                                    slist4.extend([4]*rk6[f41][f42][f43][f44+1][f45])
                                                                if(rk6[f41][f42][f43][f44][f45+1]>0):
                                                                    slist4.extend([5]*rk6[f41][f42][f43][f44][f45+1])
                                                                mslist=list(itertools.product(slist1,slist2,slist3,slist4))
                                                                check=0
                                                                for pair in mlist:         
                                                                    a=pair.count(1)
                                                                    b=pair.count(2)
                                                                    c=pair.count(3)
                                                                    d=pair.count(4)
                                                                    check=check+rk5[a][b][c][d]*(rk5[a][b][c][d]-1)
                                                                for pair in mslist:
                                                                    a=pair.count(1)
                                                                    b=pair.count(2)
                                                                    c=pair.count(3)
                                                                    d=pair.count(4)
                                                                    e=pair.count(5)
                                                                    check=check-rk6[a][b][c][d][e]*(rk6[a][b][c][d][e]-1)
                                                                if(check==0):
                                                                    check1=1
                                                                    zero=[f11,f12,f13,f14,f21,f22,f23,f24,f31,f32,f33,f34,f41,f42,f43,f44]
                                                                if(check>0):                                                                    
                                                                    check2=1
                                                                    positive=[f11,f12,f13,f14,f21,f22,f23,f24,f31,f32,f33,f34,f41,f42,f43,f44]
                                                                if(check<0):
                                                                    check3=1
                                                                    negative=[f11,f12,f13,f14,f21,f22,f23,f24,f31,f32,f33,f34,f41,f42,f43,f44]
                if(check1==1 and check2==1):
                    nonample.append([n,i,j,k,l])
                    nonample.append(zero)
                    nonample.append(positive)
                if(check2==1):
                    nonzero.append([n,i,j,k,l])
                if(check3==1):
                    nonnef.append([n,i,j,k,l])
        print(i)
print(nonzero)
print(nonample)
print(nonnef)


