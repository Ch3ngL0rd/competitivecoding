# d,a,b = map(int,input().split())

# find combinations where digits removed sum to targetSum and return the combinations
# digits is a string, targetSum is an number
def findCombinations(digits, targetSum):
    combinations = []
    for i in range(0, 2**len(digits)):
        binary = bin(i)[2:].zfill(len(digits))
        remainingDigits = ''
        sumDigits = 0
        for index, bit in enumerate(binary):
            if bit == '1':
                sumDigits += int(digits[index])
            else:
                remainingDigits += digits[index]
        if sumDigits == targetSum:
            combinations.append(remainingDigits)
    return combinations

# returns the expected value of digits
def dfs(digits,maximise=True):
    # base case is when digits is 0, or it has no combinations
    if len(digits) == 0:
        return 0
    
    totalSum = 0
    for i in range(2,13):
        if i <= 7:
            frequency = i - 1
        else:
            frequency = 12 - i + 1
        combinations = findCombinations(digits,i)
        if len(combinations) == 0:
            totalSum += frequency * int(digits)
        else:
            expected = [dfs(combination) for combination in combinations]
            value = max(expected) if maximise else min(expected)
            totalSum += value * frequency
    
    return totalSum / 36
    
print(dfs(str(1239)))