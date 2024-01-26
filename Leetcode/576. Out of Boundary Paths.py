'''
Thoughts:
For each square, we calculate the distance to edge for each position?
- array of (distance to edge, amount)
- nah how many have min distance - (distance,amount)
State can be number of moves left
- going back is like 1 == 1, 3 == 2, 5 == 3, (x+1)//2 - if min distance is one
- lets say it was min distance = 2
(x-mindistance + 2)//2
- 1 == 0, 2 == 1, 3 == 1, 4 == 2, 5 == 3 yep formula is good
# unless its a "1x1" box - where you cant hop back
# given min distance and number of steps allowed,
paths = (n_steps - min_distance + 2) // 2
- why do we divide it by two?
[x] with n = 1 is 4
[x -]
[- -]
with n = 1 is 2, because there are 2 with min_distance n = 1
[(2,2) (1,2)]
[(1,2) (1,2)]
with n = 1,
state: distance to edge, number with distance to edge for n = x
dyanmic programming 1->n?
x = 1 -> 1
x = 2 -> 1
kinda thinking about it as a 3d cube, where each layer represents a different 'n' value
time complexity: O(n^3)
n = 1
2 1 2
1 0 1
2 1 2

n = 2
2 4 2
4 4 4
2 4 4

n = 1
2 2
2 2

n = 2
4 4
4 4

if we start top right, with maxSteps = 2
    for n = 1 theres 2 for 0,0
    for n = 2 theres 4 for 0,0
so total = 6
maxSteps = 3, m = 1, n = 3 start = 0,1
n = 1
3 2 3

n = 2
2 6 2

n = 3
6 4 6
if we start in the middle with maxSteps = 3:
    for n = 1, theres 2
    for n = 2, theres 6
    for n = 3, theres 4
    for a total of 12

Each layer represents how many ways from that square to the edge with that amount of n
m is always down, n is to the right
# n = 1, value = (x == 0) + (x == n - 1) + (y == 0) + (y == m - 1)
# n = 2, value of own square? no, since we already counted it
# value is sum of surrounding squares?
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        # Originally forgot this edge case
        if maxMove == 0:
            return 0
        # 1. construct solution (m x n x maxMove) matrix
        # a) base case is edges = 1
        # b) then iterative case is sum of surrounding previous squares of previous n - 1
        # then we sum a single column of (startRow,startColumn)
        # Creates a 3D matrix with dimensions m, n, maxMove
        space = [[[0 for _ in range(n)] for _  in range(m)] for _ in range(maxMove)]

        # Fill out base case with edges
        for y in range(m):
            for x in range(n):
                space[0][y][x] = [x == 0,y == 0,x == n - 1,y == m - 1].count(True)

        # Make his faster by only computing necessary
        # negative from maxMove pyramid...
        for move in range(1,maxMove):
            for y in range(m):
                for x in range(n):
                    up = space[move-1][y-1][x] if y != 0 else 0
                    down = space[move-1][y+1][x] if y != m - 1 else 0
                    left = space[move-1][y][x-1] if x != 0 else 0
                    right = space[move-1][y][x+1] if x != n - 1 else 0
                    space[move][y][x] = sum([up,down,left,right])

        pathSum = 0
        for move in range(maxMove):
            pathSum += space[move][startRow][startColumn]

        return pathSum % MOD

assert(Solution().findPaths(2,2,2,0,0) == 6)
assert(Solution().findPaths(1,3,3,0,1) == 12)
