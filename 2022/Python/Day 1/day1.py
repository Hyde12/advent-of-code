data = []
with open("input.csv", "r") as dataFile:
    for row in dataFile:
        data.append(row.strip())

tempData = []
totals = []

for line in data:
    if line:
        tempData.append(int(line))
    else:
        totals.append(sum(tempData))
        tempData = []

totals.sort(reverse=True)

def top(num):
    i = 0
    top = []
    while i < num:
        top.append(totals[i])
        i += 1
    return sum(top)

print(top(3))