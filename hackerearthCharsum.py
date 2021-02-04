def getCharSum(given_str):
      weight = 0
      for char in given_str:
          weight+= ord(char)-96
      return weight    

given_str = input()
print(getCharSum(given_str))