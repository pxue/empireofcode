# https://github.com/Empire-of-Code-Puzzles/checkio-empire-crystal-lattice
#def golf(b):
 #k=0
 #for g in b:
  #i=0

  #for row in g:

   #s=c=0
   #for v in row:
    #if v==s:
     #return 0
    #s=v

    #if k&i==0:
     #t=0

     #for l in range(len(g if k else b)):
      #z = b[l][i][c] if not k else g[l][c]
      #if t==z:
       #return 0
      #t=z

    #c+=1
   #i+=1
  #k+=1
 #return 1

def golf(b):
 k=0
 for g in b:
  for r in g:
   c=0
   for v in r:
    if k<2:
     t=0
     for l in g if k else b :
      z=l[c]
      if t==z:
       return 0
      t=z
    c+=1
  k+=1
 return 1




TESTS = [
    {
        "input": [[['X', 'Z'], ['Z', 'X']], [['Z', 'X'], ['X', 'Z']]],
        "answer": True,
    },
    {
        "input": [[['X', 'Z'], ['Z', 'X']], [['X', 'Z'], ['Z', 'X']]],
        "answer": False,
    },
    {
        "input": [
                    [
                        ['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']
                    ],
                    [
                        ['Z', 'X', 'Z'], ['X', 'Z', 'X'], ['Z', 'X', 'Z']
                    ],
                    [
                        ['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']
                    ]
                ],
        "answer": True,
    },
    {
        "input": [[['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']],
                    [['Z', 'X', 'Z'], ['X', 'X', 'X'], ['Z', 'X', 'Z']],
                    [['X', 'Z', 'X'], ['Z', 'X', 'Z'], ['X', 'Z', 'X']]],
        "answer": False,
    },
    {
        "input": [[['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                    ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                    [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                    [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                    ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                    [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                    [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                    ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']]],
        "answer": True,
    },
    {
        "input": [[['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                    [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                    ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                    [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                    [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                    ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                    [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']]],
        "answer": True,
    },
    {
        "input": [[['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                    [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                    [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                    [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                    ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                    [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']]],
        "answer": False,
    },
    {
        "input": [[['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']],
                    [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                    ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                    [['Z', 'X', 'Z', 'X', 'Z'], ['Z', 'X', 'Z', 'X', 'Z'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['Z', 'X', 'Z', 'X', 'Z'], ['Z', 'X', 'Z', 'X', 'Z']],
                    [['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'],
                    ['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X']],
                    [['Z', 'X', 'Z', 'X', 'Z'], ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z'],
                    ['X', 'Z', 'X', 'Z', 'X'], ['Z', 'X', 'Z', 'X', 'Z']]],
        "answer": False,
    },
]

for i, t in enumerate(TESTS):
    assert golf(t["input"]) == t["answer"], i
