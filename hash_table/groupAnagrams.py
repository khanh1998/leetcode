class Solution:
    def groupAnagrams(self, strs: list):
        anagramToIndex = {}
        data = []
        anagramIndex = 0
        for str in strs:
            key = [0] * 26
            # convert the letter to a number, start from 0
            # get the relative index of current letter, count from a
            for letter in str:
                index = ord(letter) - ord('a')
                key[index] += 1
            key = tuple(key)
            if key in anagramToIndex:
                data[anagramToIndex[key]].append(str)
            else:
                anagramToIndex[key] = anagramIndex
                anagramIndex += 1
                data.append([str])
        return data

solution = Solution()
print(solution.groupAnagrams(["ddddddddddg","dgggggggggg"]))