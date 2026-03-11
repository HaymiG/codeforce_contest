t = int(input())
sum = 0
Tetrahedron = 4
Cube = 6
Octahedron = 8
Dodecahedron = 12
Icosahedron = 20
for i in range(t):
  n = input()
  if n == "Icosahedron":
    sum += 20
  elif n == "Dodecahedron":
    sum += 12
  elif n == "Octahedron":
    sum += 8
  elif n == "Cube":
    sum += 6
  elif n == "Tetrahedron":
    sum += 4
  else:
    sum += 0
print(sum)
  




