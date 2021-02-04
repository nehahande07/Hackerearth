def solve (A):
    # Write your code here
    mid = N//2
    generated_num = ''
    A = list(A)
    for num in A[:mid]:
        generated_num += str(num)[0]
    for num in A[mid:]:
        generated_num += str(num)[-1]
    remainder = int(generated_num) %11
    if remainder ==0:
        return  "OUI"
    else:
        return  "NON"


N = int(input())
A = map(int, input().split())


out_ = solve(A)
print (out_)