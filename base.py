# itératif

def decTob(n,b):
  assert (b>1 and b<17), "b doit être compris entre 2 et 16"
  signes = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
  mot = ""
  while n!=0:
    mot = signes[n%b] + mot
    n = n//b
  return mot

print(decTob(15,16))

 # récursive

def decTobr(n,b):
  signes = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
  if n//b==0:
    return signes[n%b]
  else :
    return decTobr(n//b,b)+signes[n%b]
  

# -------------------------------------------------------------------------

# itératif

def bTodec(mot,b):
  assert (b>1 and b < 17), "b doit être compris entre 2 et 16"
  assert (type(mot) == str), "Le nombre n doit être une chaîne de caractères"
  signes = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
  resul = 0
  p = len(mot)
  for i in range(p):
    resul = resul + signes.index(mot[i])*b**(p-i-1)
  return resul

print(bTodec("10011",2))
print(bTodec("4D",16))

# récursive

def bTodecr(mot,b):
  assert (b>1 and b < 17), "b doit être compris entre 2 et 16"
  assert (type(mot) == str), "Le nombre n doit être une chaîne de caractères"
  signes = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
  p = len(mot)
  
  if len(mot) == 1:
    return signes.index(mot[0])*b**0
  else:
    return bTodecr(mot[1:],b) + signes.index(mot[0])*b**(len(mot)-1)
  

print(bTodecr("10011",2))  

