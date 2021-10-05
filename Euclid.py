
def euclidsGCD_Func(a,b):
  c = a%b
  while c:
    a = b
    b = c
    c = a%b
  print(c)
  return c

  