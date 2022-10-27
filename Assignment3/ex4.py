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

    rowsum.append(0)
    for e in matrix[i]:
        rowsum[i] += e

    if i == 0:
        colsum = copy.deepcopy(matrix[0])
    else:
        for b in range(0, len(matrix[i])):
            colsum[b] += matrix[i][b]

    if i > 0 and len(matrix[i]) < len(matrix[0]):
        matrix[i] += (len(matrix[0]) - len(matrix[i])) * [0]
    i += 1


for e in rowsum:
    totsum += e

print("[", end="")
for l in matrix:
    if l == matrix[-1]:
        print(l, end="")
    else:
        print(l)
print("]")

print("row sums: ", rowsum)
print("column sums: ", colsum)
print("total sum: ", totsum)
