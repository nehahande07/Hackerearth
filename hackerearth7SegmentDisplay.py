testCases = int(input())
for i in range(testCases):
    number = str(input())
    numofsticks = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
    totalSticks = 0
    result = ''

    for digit in number:
         totalSticks += numofsticks[digit]

    if (totalSticks%2) == 0 :
        for i in range(int(totalSticks/2)):
             result+='1'
    else:
         remainingSticks =int((totalSticks-3)/2)
         for i in range(remainingSticks):
             result += '1'
         result = '7'+ result

    print(result)                  