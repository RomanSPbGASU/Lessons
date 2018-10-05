print("Исходная матрица")
matrix = [[0.5,0,0,0,0],
          [1,0.5,0,0,0],
          [1,1,0.5,0,0],
          [1,1,1,0.5,0],
          [1,1,1,1,0.5]]
for line in matrix:
    print(line)
print("Транспонированная матрица")
transpoze = zip(*matrix)
for line in transpoze:
    print(line)