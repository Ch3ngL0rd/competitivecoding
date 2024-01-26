# d,a,b = map(int,input().split())

# find combinations where digits removed sum to targetSum and return the combinations
# digits is a string, targetSum is an number
def findCombinations(digits,targetSum):
    combinations = []
    
    for i in range(0,2**len(digits)):
        binary = bin(i)[2:].zfill(len(digits))
        values = ''
        missingSum = 0
        for index,bit in enumerate(binary):
            if bit == '1':
                values += digits[index]
            else:
                missingSum += int(digits[index])
        if missingSum == targetSum:
            if values == '':
                combinations.append('0')
            else:
                combinations.append(values)
    
    return combinations

# returns the expected value of digits
def dfs(digits):
    # base case is when digits is 0, or it has no combinations
    if len(digits) == 0:
        return int(digits)

    totalSum = 0
    for i in range(2,13):
        if i < 7:
            frequency = i - 1
        else:
            frequency = 12 - i + 1
        combinations = findCombinations(digits,i)
        if len(combinations) == 0:
            totalSum += frequency * int(digits)
        else:
            print(combinations,digits,i)
            for combination in combinations:
                totalSum += frequency * dfs(combination) / len(combinations)
    
    return totalSum / 36
    
# print(findCombinations('19',10))
print(dfs(str(1345)))