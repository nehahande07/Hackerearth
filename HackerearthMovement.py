# Input
# First and the only line contain the integer n  which denotes the position of his friend's house.

# Output
# Output contains a single line denoting the minimum number of steps.

#Link to problem
#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/a-movement-1/description/

n = int(input())
stepsCount = n//5
if(n%5 !=0):
   stepsCount +=1
  
print(stepsCount)