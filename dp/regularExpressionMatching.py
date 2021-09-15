from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        first_row = []
        second_row = [True]
        for i in range(len(s)):
            second_row.append(False)
        EMPTY = '_'
        s = EMPTY + s
        p = EMPTY + p
        print(first_row)
        print(second_row)
        for j in range(1, len(p)):
            third_row = [False for _ in range(len(s))]
            for i in range(len(s)):
                if s[i] == p[j]:
                    third_row[i] = second_row[i-1]
                elif p[j] == '.':
                    if i > 0:
                        third_row[i] = second_row[i-1]
                    else:
                        third_row[i] = False
                elif p[j] == '*':
                    if p[j-1] == s[i] or p[j-1] == '.':
                        if i > 0:
                            third_row[i] =  second_row[i] or third_row[i - 1] or first_row[i]
                        else:
                            third_row[i] =  second_row[i] or first_row[i]
                    elif p[j-1] != s[i]:
                        # check if first row exist
                        #   _ a b c
                        # _ t f f f
                        # e
                        # * 
                        third_row[i] = first_row[i]

                else:
                    third_row[i] = False
            print(third_row)
            first_row = [num for num in second_row]
            second_row = [num for num in third_row]
        return third_row[-1]

s = Solution()
#  _ a b
#_ t f f
#. f t f
#* t t
print(s.isMatch('aa', 'a*') == True)
print(s.isMatch('aa', 'a') == False)
print(s.isMatch('ab', '.*') == True)
print(s.isMatch('aab', 'c*a*b') == True)
print(s.isMatch('mississippi', 'mis*is*p*.') == True)