class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        counts = [[False]*length for _ in range(length)]
        count = 0
        j_base = 0
        i, j = 0, j_base
        while j_base < length:
            if i == j:
                counts[i][j] = True
                count += 1
            else:
                if s[i] == s[j] and (counts[i+1][j-1] == True or j-i == 1):
                    counts[i][j] = True
                    count += 1
            i, j = i + 1, j + 1
            if i >= length or j >= length:
                j_base += 1
                i, j = 0, j_base
        
        return count

s = Solution()
print(s.countSubstrings('b') == 1)
print(s.countSubstrings('bb') == 3)
print(s.countSubstrings('ba') == 2)
print(s.countSubstrings('aaa') == 6)
print(s.countSubstrings('aba') == 4)
print(s.countSubstrings('bba') == 4)
print(s.countSubstrings('abb') == 4)
print(s.countSubstrings('abc') == 3)
print(s.countSubstrings('abcd') == 4)
print(s.countSubstrings('aacd') == 5)
print(s.countSubstrings('abbd') == 5)
print(s.countSubstrings('abcc') == 5)
print(s.countSubstrings('abba') == 6)
print(s.countSubstrings('aabb') == 6)