from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        str_len = len(s)
        word_len = len(words[0])
        words_num = len(words)
        if str_len < word_len:
            return []
        res = []
        # count occurrence number of each word in array
        words_count = {}
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1
        # main loop
        for i in range(str_len - word_len + 1):
            word_flags = {} # occurence number of words in current substring
            isBreak = False
            for j in range(words_num):
                start = i + j * word_len
                end = start + word_len
                search = s[start:end]
                if word_flags.get(search, 0) >= words_count.get(search, -1):
                    isBreak = True
                    break
                else:
                    word_flags[search] = word_flags.get(search, 0) + 1
            if not isBreak:
                res.append(i)
        return res

s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo","bar"]) == [0,9])
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == [])
print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6,9,12])
print(s.findSubstring("aaaaaaaaaa", ["aaaaa"]) == [0,1,2,3,4,5])
print(s.findSubstring("bbbbbbbbaaaaaaaaaa", ["aaaaa"]) == [8,9,10,11,12,13])
print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]) == [8])