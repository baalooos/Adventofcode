f = open("input.txt", "r")

digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digit_translate = [{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3}, {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}]
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
