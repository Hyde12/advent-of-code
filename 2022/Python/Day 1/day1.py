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

print(totals[0])