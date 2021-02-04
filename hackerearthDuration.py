N=int(input())

for i in range(N):
    SH,SM,EH,EM=map(int,input().split())

    a=SH*60+SM

    b=EH*60+EM

    c=abs(b-a)

    print(c//60, c%60)