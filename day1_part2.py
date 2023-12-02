codes = [i[:-1] for i in open("input.txt")]

"""
codes = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen",
"648211",
"dmgnq6"]
"""

#codes = ["27four", "648211", "eightwothree", "dmgnq6", "dbxdgtone", "two8twoklgnrm"] #267

#codes = ["two8twoklgnrm"]

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
stringToDigit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

total = 0

for code in codes:
    calibrationValue = 0
    
    firstDigitIndex = None
    secondDigitIndex = None
    firstStrDigit = [None, ""]
    secondStrDigit = [None, ""]

    for digit in digits:
        firstStrDigitIndex = code.find(digit)
        lastStrDigitIndex = code.rfind(digit)
        if firstStrDigitIndex < 0:
            continue

        if firstStrDigit[0] == None and secondStrDigit[0] == None:            
            firstStrDigit = [firstStrDigitIndex, digit]
            secondStrDigit = [lastStrDigitIndex, digit]
            
        if firstStrDigit[0] > firstStrDigitIndex:
            firstStrDigit = [firstStrDigitIndex, digit]

        
        if secondStrDigit[0] < lastStrDigitIndex:
            secondStrDigit = [lastStrDigitIndex, digit]
        
    for index in range(len(code)):
        try:
            int(code[index])
            if firstDigitIndex == None:
                firstDigitIndex = index
                
            secondDigitIndex = index
        except ValueError:
            continue

    
    
    if firstDigitIndex != None and secondStrDigit[0] != None:
        if firstDigitIndex < firstStrDigit[0]:
            calibrationValue = int(code[firstDigitIndex]) * 10
        else:
            calibrationValue = stringToDigit[firstStrDigit[1]] * 10
    elif secondStrDigit[0] != None:
        calibrationValue = stringToDigit[firstStrDigit[1]] * 10
    else:
        calibrationValue = int(code[firstDigitIndex]) * 10
        
    if secondDigitIndex != None and secondStrDigit[0] != None:    
        if secondDigitIndex > secondStrDigit[0]:
            calibrationValue += int(code[secondDigitIndex])
        else:
            calibrationValue += stringToDigit[secondStrDigit[1]]
    elif secondStrDigit[0] != None:
        calibrationValue += stringToDigit[secondStrDigit[1]]
    else:
        calibrationValue += int(code[secondDigitIndex])
    
    total += calibrationValue

print(total)
