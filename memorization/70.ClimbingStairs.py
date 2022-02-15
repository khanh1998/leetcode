class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        fibo1 = 0
        fibo2 = 1
        while i < n:
            fibo3 = fibo1 + fibo2
            fibo1 = fibo2
            fibo2 = fibo3
            i += 1
        return fibo2
        