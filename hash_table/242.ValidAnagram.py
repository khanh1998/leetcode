class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letterCount = {}
        for letter in s:
            if letter in letterCount:
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1
        
        for letter in t:
            if letter in letterCount:
                if letterCount[letter] > 0:
                    letterCount[letter] -= 1
                else:
                    return False
            else:
                return False
        
        return True

s = Solution()
print(s.isAnagram('anagram', 'nagaram') == True)
print(s.isAnagram('rat', 'car') == False)
print(s.isAnagram('r', 'r') == True)
print(s.isAnagram('rv', 'vr') == True)
print(s.isAnagram('vv', 'vr') == False)