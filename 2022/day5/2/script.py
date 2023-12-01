f = open("input.txt", "r")

score = 0

q = []
for i in range(9):
    q.append([])

tab = f.readlines()
#for line in f:
iter = 0
for i in tab:
    if i[1] == "1":
        break
    iter+= 1

for i in range(iter-1, -1, -1):
    try:
        if tab[i][1] != " ":
            q[0].append(tab[i][1])
    except:
        exception = 'yes'
    try:
        if tab[i][5] != " ":
            q[1].append(tab[i][5])
    except:
        exception = 'yes'
    try:
        if tab[i][9] != " ":
            q[2].append(tab[i][9])
    except:
        exception = 'yes'
    try:
        if tab[i][13] != " ":
            q[3].append(tab[i][13])
    except:
        exception = 'yes'
    try:
        if tab[i][17] != " ":
            q[4].append(tab[i][17])
    except:
        exception = 'yes'
    try:
        if tab[i][21] != " ":
            q[5].append(tab[i][21])
    except:
        exception = 'yes'
    try:
        if tab[i][25] != " ":
            q[6].append(tab[i][25])
    except:
        exception = 'yes'
    try:
        if tab[i][29] != " ":
            q[7].append(tab[i][29])
    except:
        exception = 'yes'
    try:
        if tab[i][33] != " ":
            q[8].append(tab[i][33])
    except:
        exception = 'yes'

print(q)
iter = iter + 2

for i in range (iter, len(tab)):
    line = tab[i].split(" ")
    nombre = int(line[1])
    fromm = int(line[3])
    to = int(line[5])

    temp = []
    for i in range(int(line[1])):
        temp.append(q[fromm - 1].pop(-1))


    for i in range(len(temp)):
        q[to - 1].append(temp.pop(-1))

    print(temp)
    print(q)

rep = ""
for i in q:
    rep += i[-1]

print(rep)
