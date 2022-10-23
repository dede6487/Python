fnames = ["file7.txt", "file1.png", "file3.txt", "file2.txt","file7.txt", "file1.txt", "file3.txt",
          "file4.png","file4.png", "file5.txt", "file0.txt", "file7.dat"]

fnames = list(set(fnames))

remove = []

for c in fnames:
    if ".txt" not in c:
        remove.append(fnames.index(c))

for i in reversed(remove):
    fnames.remove(fnames[i])

fnames = sorted(fnames)

print(fnames)
