import copy

matrix = []
rowsum = []
colsum = []
totsum = 0

i = 0
while True:
    row = input("Enter row: ")
    if row == "x":
        break
    matrix.append([])
    matrix[i].extend(int(a) for a in row.split())

    for j in range(0, i):
        if len(matrix[i]) < len(matrix[j]):
            matrix[i] += (len(matrix[j]) - len(matrix[i])) * [0]
        elif len(matrix[i]) > len(matrix[j]):
            matrix[j] += (len(matrix[i]) - len(matrix[j])) * [0]

    rowsum.append(0)
    for e in matrix[i]:
        rowsum[i] += e

    if i == 0:
        colsum = list(copy.deepcopy(matrix[0]))
    else:
        for b in range(0, len(matrix[i])):
            if len(matrix[i]) > len(colsum):
                for m in range(0,len(matrix[i]) - len(colsum)):
                    colsum.append(0)
            colsum[b] += matrix[i][b]

    i += 1

for e in rowsum:
    totsum += e

print("[", end="")
for l in matrix:
    print("[", end="")
    for e in range(0, len(l)):
        if e != l:
            print(l[e], end=" ")
        else:
            print(l[e], end="")
    if l is not matrix[-1]:
        print("]\n ", end="")
    else:
        print("]", end="")
print("]")

print("row sums: ", rowsum)
print("column sums: ", colsum)
print("total sum: ", totsum)
