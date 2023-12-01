input = open("input.txt", "r")

calibratedValuesPart1 = []
calibratedValuesPart2 = []

for line in input:
    lineNumPart1 = ""
    lineNumPart2 = ""
    buffer = ""
    if line == "\n":
        continue
    for char in line:
        if char.isnumeric():
            lineNumPart1 += char
            lineNumPart2 += char
            buffer = ""
        if char.isalpha():
            buffer += char
        if buffer.endswith("one"): lineNumPart2 += "1"
        if buffer.endswith("two"): lineNumPart2 += "2"
        if buffer.endswith("three"): lineNumPart2 += "3"
        if buffer.endswith("four"): lineNumPart2 += "4"
        if buffer.endswith("five"): lineNumPart2 += "5"
        if buffer.endswith("six"): lineNumPart2 += "6"
        if buffer.endswith("seven"): lineNumPart2 += "7"
        if buffer.endswith("eight"): lineNumPart2 += "8"
        if buffer.endswith("nine"): lineNumPart2 += "9"
        
    print("Raw value part 1: ", lineNumPart1)
    print("Raw value part 2: ", lineNumPart2)
    addedValPart1 = lineNumPart1[0] + lineNumPart1[len(lineNumPart1) - 1]
    addedValPart2 = lineNumPart2[0] + lineNumPart2[len(lineNumPart2) - 1]
    print("Calibrated value part 1: ", addedValPart1)
    print("Calibrated value part 2: ", addedValPart2)
    calibratedValuesPart1.append(addedValPart1)
    calibratedValuesPart2.append(addedValPart2)

sumCalibratedValuePart1 = 0
for value in calibratedValuesPart1:
    sumCalibratedValuePart1 += int(value)

sumCalibratedValuePart2 = 0
for value in calibratedValuesPart2:
    sumCalibratedValuePart2 += int(value)

print("Total calibrated value part 1: ", sumCalibratedValuePart1)
print("Total calibrated value part 2: ", sumCalibratedValuePart2)
