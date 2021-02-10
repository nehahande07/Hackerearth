# Input format

# First line: A single integer N denoting the size of array 
# Second line: N space-separated integers.

# Output format
# If the number is divisible by 10, then print Yes. Otherwise, print No.

#Link to the problem description
#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/description/


N = int(input())
data = [int(x) for x in input().split()]


lastDigit =''
for num in data:
    lastDigit += str(num % 10)
if(int(lastDigit)%10 ==0):
    ans ="Yes"
else:
    ans= "No"       

print(ans)