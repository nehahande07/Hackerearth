from sys import stdin

 

N, Q = map(int, stdin.readline().split())

A = list(map(int, stdin.readline().split()))

 

B = [0]

for elements in A:
        B.append(elements+B[-1])

print(B) 

for _ in range(Q):

        L, R = map(int, stdin.readline().split())

        print((B[R]-B[L-1])//(R-L+1))