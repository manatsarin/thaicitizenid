#!/usr/bin/python


def validate(id):
  if len(id) != 13:
    return False
  else:
    sum = 0
    for i in range(12):
      sum = sum + int(id[i])*(13-i)
      #print(id[i], i, 13-i, int(id[i])*(13-i), sum)
    if ((11 - (sum % 11)) % 10) != int(id[12]):
      #print("Invalid check sum!", (sum % 11))
      return False
    return True


if validate("4928347404300"):
   print('OK')
else:
   print('Incorrect')

