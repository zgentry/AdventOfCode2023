input = open("input.txt", "r")

calibratedValues = []

for line in input:
    lineNum = ""
    if line == "\n":
        continue
    for char in line:
        if char.isnumeric():
            lineNum += char
        
    print("Raw value: ", lineNum)
    addedVal = lineNum[0] + lineNum[len(lineNum) - 1]
    print("Calibrated value: ", addedVal)
    calibratedValues.append(addedVal)

sumCalibratedValue = 0
for value in calibratedValues:
    sumCalibratedValue += int(value)

print("Total calibrated value part 1: ", sumCalibratedValue)