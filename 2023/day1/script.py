f = open("input.txt", "r")

digit = [{O, zero}, {1, }]

tab = []
sum = 0

for i in f:
    first = False
    first = 0
    last = ""
    for j in i:
        if j != "\n":
            if j.isdigit():
                if not first:
                    first = j
                else:
                    last = j
        else:
            if last == "":
                tab.append(str(first) + str(first))
            else:
                tab.append(str(first) + str(last))

sum = 0
print(len(tab))

for i in tab:
    sum += int(i)

print(sum)
