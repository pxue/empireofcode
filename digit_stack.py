def golf(d):
 q=[];s=0
 for c in d:
  if "U" in c:
   q+=[int(c[-1])]
  elif len(q):
   if "O" in c:
    s+=q.pop()
   else:
    s+=q[-1]
 return s
