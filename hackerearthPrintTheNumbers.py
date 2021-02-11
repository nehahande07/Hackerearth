# Input:
# First line contains integer N - denoting total count of numbers that are to be printed.
# Second line contains N space separated integers.

# Output:
# Print the numbers in input.

#Link to the problem:
#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/print-the-numbers/description/

N = int(input())
numbers = [int(i) for i in input().split()]
print(*numbers)