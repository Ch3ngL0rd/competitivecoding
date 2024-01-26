d, F = input().split()

added = False
newF = ''
for index, number in enumerate(F):
    if int(d) > int(number):
        newF = F[0:index] + d + F[index:]
        added = True
        break
    
if not added:
    newF = F + d
    
print(newF)