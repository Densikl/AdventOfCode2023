codes = [i[:-1] for i in open("input.txt")]

calibrationValue = 0

for code in codes:
    first = None
    second = None
    for symbol in code:
        try:
            int(symbol)
            if first == None:
                first = symbol  
            second = symbol

        except ValueError:
            continue
    if first != None and second != None:
        calibrationValue += int(first + second)
    elif first != None:
        calibrationValue += int(first*2)
    
print(calibrationValue)
