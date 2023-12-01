f = open("input.txt", "r")

tab = []
sum = 0

for i in f:
    if i != "\n":
        sum += int(i.strip("\n"))
    #print(i.strip("\n"))
    else:
        tab.append(sum)
        sum = 0

tab.sort()
print(tab)
total = tab[-1] + tab[-2] + tab[-3]
print(total)
