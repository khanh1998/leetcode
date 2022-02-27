from operator import sub
from typing import Counter


class Solution:
    def minWindow1(self, s: str, t: str) -> str:
        # time limit exceeded
        mapping = {}
        for letter in t:
            if mapping.get(letter, None):
                mapping[letter] += 1
            else:
                mapping[letter] = 1
        res = None 
        for outer in range(len(s)):
            matched_letter = 0
            tmp_map = { **mapping }
            for inner in range(outer, len(s)):
                if tmp_map.get(s[inner], None):
                    if tmp_map[s[inner]] > 0:
                        tmp_map[s[inner]] -= 1
                        if tmp_map[s[inner]] == 0:
                            matched_letter += 1
                if matched_letter == len(mapping):
                    substring_length = inner - outer + 1
                    if res == None or substring_length < len(res):
                        res = s[outer:inner + 1]
                        print(res)
                    break
        return res if res != None else ""
    def minWindow(self, s: str, t: str) -> str:
        # using sliding window
        mapping = {}
        for letter in t:
            if mapping.get(letter, None):
                mapping[letter] += 1
            else:
                mapping[letter] = 1
        letter_matched_count = 0
        res = None 
        left, right = 0, -1
        current_map = {}
        while not (right == len(s) - 1 and letter_matched_count < len(mapping)):
            if letter_matched_count < len(mapping):
                right += 1
                if not mapping.get(s[right], None):# the letter at the right pointer is not in target string
                    continue
                if current_map.get(s[right], None):
                    current_map[s[right]] += 1
                else:
                    current_map[s[right]] = 1
                if current_map[s[right]] == mapping[s[right]]:# if the count for current letter reach the threshold
                    letter_matched_count += 1
            if letter_matched_count == len(mapping):
                if mapping.get(s[left], None):# if the letter at the left pointer is in the target string
                    if current_map.get(s[left]) == mapping.get(s[left]): # it gonna be bellow the threshold soon
                        letter_matched_count -= 1
                    if current_map.get(s[left], -1):
                        current_map[s[left]] -= 1
                substring_len = right - left + 1
                if res == None or substring_len < len(res):
                    res = s[left: right + 1]
                left += 1
        return res if res else ''

s = Solution()
print(s.minWindow('ADOBECODEBANC', 'ABC') == "BANC")
print(s.minWindow('BACDOBECODEBANC', 'ABC') == "BAC")
print(s.minWindow('DFCDOBEBCAODEBANC', 'ABC') == "BCA")
print(s.minWindow('a', 'a') == 'a')
print(s.minWindow('a', 'aa') == '')
print(s.minWindow('aa', 'aa') == 'aa')