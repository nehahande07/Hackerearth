# Input:

# 2 integers-

# First denoting length of Secret Book.
# Second is number of pages in Book.

# Output:
# If Cheeku should take medicine, print - "Take Medicine"
# Else print - "Don't take Medicine".

# Link to the problem:
#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/doctors-secret/description/


lengthOfBook, noOfPages = [int(x) for x in input().split()]
if(lengthOfBook<=23 and (noOfPages>500 or noOfPages<1000)):
    print("Take Medicine")
else:
    print("Don't take Medicine")   