def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
    
testcases = int(input())  
str1 = []
str2 =[]
fre1 = []
fre2 = []


for i in range(testcases):
    str1, str2 =input().split()
    #str2 = input()
    fre1 = char_frequency(str1)
    fre2 = char_frequency(str2)
    if(fre1 == fre2):
        print("YES")
    else:
        print("NO")