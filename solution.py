def FirstReverse(strParam):
  newStr = ""

  for letter in reversed(strParam):
    newStr = newStr + letter

  return newStr
 
print(FirstReverse(input()))
