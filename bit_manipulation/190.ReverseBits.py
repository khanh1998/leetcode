class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            rightMostBit = n & 1
            result |= rightMostBit
            n = n >> 1
            if i < 31:
                result = result << 1
        print(format(n, '032b'))
        print(format(result, '032b'))
        return result

s = Solution()
print(s.reverseBits(5))