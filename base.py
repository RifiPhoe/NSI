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
