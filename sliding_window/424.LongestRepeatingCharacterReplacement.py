class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        if length <= 1:
            return length
        max_count = 0
        counts = [0] * 26
        def inc_count(char: str):
            nonlocal counts
            counts[ord(char) - 65] += 1
        def dec_count(char: str):
            nonlocal counts
            counts[ord(char) - 65] -= 1
        def get_count(char: str):
            nonlocal counts
            return counts[ord(char) - 65]
        max_len = 0
        left, right = 0, 0
        inc_count(s[0])
        while right <= length - 1:
            window_len = right - left + 1
            # max_count = max(max_count, get_count(s[left]))
            max_count = max(counts)
            if window_len - max_count <= k:
                max_len = max(window_len, max_len)
                right += 1
                if right <= length - 1:
                    inc_count(s[right])
            else:
                dec_count(s[left])
                left += 1

        return max_len

s = Solution()
print(s.characterReplacement('AABABBA', 1) == 4)
print(s.characterReplacement('AABABBA', 2) == 5)
print(s.characterReplacement('BAAAAA', 1) == 6)
print(s.characterReplacement('AAAAA', 2) == 5)
print(s.characterReplacement('AAAAA', 0) == 5)
print(s.characterReplacement('AAAAAB', 1) == 6)
print(s.characterReplacement('BAABAAAB', 2) == 7)
print(s.characterReplacement('ABAB', 2) == 4)
print(s.characterReplacement('ABCD', 0) == 1)
print(s.characterReplacement('ABCD', 1) == 2)
print(s.characterReplacement('ABCD', 2) == 3)
print(s.characterReplacement('ABCD', 3) == 4)
print(s.characterReplacement('ABCD', 4) == 4)