

# Using readlines()
file1 = open('output', 'r')
Lines = file1.readlines()

count = 0
arr = []
for line in Lines:
    line = line.strip()
    if line.startswith("<Duplicate Cost"):
        arr.append(" ")
        arr.append("Duplicate")

    if line.startswith("<FileName>"):
        arr.append(line.split("FileName")[1][1:-1][:-1])

    if line.startswith("<LineRange"):
        arr.append("".join(line.split("LineRange")[1:-1]).strip()[:-3])



with open("parsed.txt", "w") as fp:
    for line in arr:
        fp.write(line)
        fp.write("\n")



