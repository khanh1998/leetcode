class Solution:
    def numDecodings(self, s: str) -> int:
        NUM = 1000000007
        length = len(s)
        a = [0] * (length + 1)
        a[0] = 1
        a[1] = self.ways_one(s[0])
        i = 2
        while i < length + 1:
            one_char_ways = self.ways_one(s[i - 1]) * a[i - 1]
            two_chars_ways = self.ways_two(s[i - 2], s[i - 1]) * a[i - 2]
            a[i] = (one_char_ways + two_chars_ways) % NUM
            i += 1
        return a[length]

    def ways_one(self, c: chr) -> int:
        if c == '*':
            return 9
        elif c != '0':
            return 1
        else:
            return 0
    def ways_two(self, curr: chr, front: chr) -> int:
        if curr == '*' and front == '*':
            return 15
        elif curr == '*':
            # case *D
            return 1 if int(front) > 6 else 2
        elif front == '*':
            # case D*
            if curr == '1':
                return 9
            elif curr == '2':
                return 6
            else:
                return 0
        else:
            val = int(curr + front)
            return 1 if val >= 10 and val <= 26 else 0

solution = Solution()
print(solution.numDecodings('1*'))
