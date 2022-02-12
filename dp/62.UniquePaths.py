# watch this awesome explaination: https://www.youtube.com/watch?v=IlEsdxuD4lY

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        count = 1
        while count < m:
            for i in reversed(range(0, n -1)):
                row[i] = row[i + 1] + row[i]
            count += 1
        return row[0]

s = Solution()

print(s.uniquePaths(3, 7) == 28)
print(s.uniquePaths(3, 2) == 3)
print(s.uniquePaths(1,1) == 1)
print(s.uniquePaths(1,2) == 1)
print(s.uniquePaths(2,1) == 1)
print(s.uniquePaths(2,2) == 2)
            