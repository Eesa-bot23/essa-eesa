def palind(r):
 e=len(r)-1
 s=0
while (s<e):
 if(r[s]!=r[e]):
  s+=1
  e-=1
return False
r=(1,2,3,3,2,1)
if(palind(r)):
print("The tuple is a flip-flop!")
else:
print("The tuple is not a flip flop")