# https://leetcode.com/problems/longest-palindromic-substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        arr = [[0 for i in range(length)] for j in range(length)]
        # init value for the array
        for i in range(length):
            arr[i][i] = 1 # substring from i to i
        # calculate
        for diagonal in range(1, length):
            for elem in range(length - diagonal):
                i = elem
                j = elem + diagonal
                print(i, j)
                innerString = arr[i+1][j-1] if j - i > 1 else True
                boundary = s[i] == s[j]
                if boundary and innerString:
                    arr[i][j] = 1
        
        for row in arr:
            print(row)
        
        # get result
        max_start, max_end, max_length = 0, 0, 1
        for start in range(length):
            for end in range(start, length):
                if arr[start][end] == 1:
                    substr_length = end - start + 1
                    if substr_length > max_length:
                        max_start = start
                        max_end = end
                        max_length = substr_length
        print(max_start, max_end, max_length)
        return s[max_start: max_end + 1]

    def longestPalindromeUpgrade(self, s: str) -> str:
        length = len(s)
        arr0 = [1 for i in range(length)] # diagonal zero
        arr1 = [] # diagonal one
        max_start, max_end, max_length = 0, 0, 1
        for diagonal in range(1, length):
            arr2 = [0 for i in range(length - diagonal)] # diagonal i th
            for index, value in enumerate(arr2):
                start = index
                end = index + diagonal
                boundary = s[start] == s[end] # two characters at the start and end position of the substring have to be the same
                hasInsideSubstring = end - start > 1
                insideSubstring = arr0[index + 1] if hasInsideSubstring else True # the inside substring is also palindromic
                # abcba, the boundaries are 'a' and 'a', the inside substring is 'bcb'
                if boundary and insideSubstring:
                    arr2[index] = 1
                    substr_length = end - start + 1
                    if substr_length > max_length:
                        max_start = start
                        max_end = end
                        max_length = substr_length
            if diagonal > 1:
                arr0 = [i for i in arr1]
            arr1 = [i for i in arr2]
            # print(arr0)
            # print(arr1)
            # print(arr2)
            # print('---------')
        return s[max_start: max_end + 1]
    def longestPalindromeMethod3(self, s: str) -> str:
        length = len(s)
        max_start, max_end, max_length = 0, 0, 1
        for base, value in enumerate(s):
            # first case: the center has one character
            biggestSubStrLength = base # biggest posibility substring length
            if (length - base - 1) < biggestSubStrLength:
                biggestSubStrLength = length - base - 1
            for i in range(1, biggestSubStrLength + 1):
                end = base + i
                start = base - i
                if s[start] != s[end]:
                    break
                else:
                    subStrLen = end - start + 1
                    if subStrLen > max_length:
                        max_start = start
                        max_end = end
                        max_length = subStrLen
            # second case: the center has two characters
            if base > 0 and s[base] == s[base - 1]:
                biggestSubStrLength = base - 1 # biggest posibility substring length
                if length - base - 1 < biggestSubStrLength:
                    biggestSubStrLength = length - base - 1
                if max_length < 2:
                    max_start = base - 1
                    max_end = base
                    max_length = 2
                for i in range(1, biggestSubStrLength + 1):
                    end = base + i
                    start = base - i - 1
                    if s[start] != s[end]:
                        break
                    else:
                        subStrLen = end - start + 1
                        if subStrLen > max_length:
                            max_start = start
                            max_end = end
                            max_length = subStrLen
        return s[max_start: max_end + 1]




s = Solution()
print(s.longestPalindromeMethod3("rfvtmdqjppztlvotnstyqeildrnevqkcoiqndxxncftlhdychrutvzkcxjnduhssfiatzisxioyuqmxqpdiouixfhyjlnfsjupwjztuyklrweuqmkuygndrqfhhcxrxcwdwcwgsknxxmxiwqxjbbljnckdgofehoarikioabmisfuzraxcaryjzsjetrvvpavbhbajrsnvrfjorjzpcjmkoekaipinfzhuaegaxzzvlwclbzhqzbtvxtgfhojqhcnokzqbedusoywsfsgbwxbvrqgmzojdmhlmzwtcvvmhnytqqlkpwyesbztabhyfukhpbchhvtzoegykvbzrywjcntrmsyokklsnzwkpjdcdcayfauuxcydiubnonpumcogiwqsqzagxhwbvkcxojfvewzqjdbbwbudxndyvubbumrktckrgxtbanatsfsxtckueqqtldfnxeznozegxnzntynlfavlmdfgpwgebylkromwrwxflgylbrtbyjblvgrxlkuhwnjmzqkngdghjvrsgtppkgsmpxrsahxlakadliwxmnbztfadwoglocbvwvhgcmgnkdtlbnqbfepbupfticejjxjoogutfvckdvztgjuklczwiimstpstbreffkvcmvofanuxndahhftbvsbfgoagwptvszptjatyoemevxnpqxboiycubeoqfenopwcbzbfnqtixtqrpzatq"))
print(s.longestPalindromeMethod3("qgecuralerljmghebsvkdxatotpbiqmxdyetorjhtmcxbgddcqwktfbpnrthsnctdmchbqqhmgtalwslepvrzsylxvlidzryqrvyoisfeqveqxivnslrtvegctcfdgfojjbohgqxxhltgaxqsfcuitjkyopbafjukbgyvkwddgbvznnvejxjlhgktoowpqlluabvhmoqnibhqlpmqgvhjdxthbhmrfrxlmxnhvhxsezehmvtxpdohjbgmnbvvemqhgaxpvytqyjrifubommzoeuqdidnmambohgegyfftsahhpoivetithnfuzppprkpovpymhqardzlohjwrfiyxcnqgdwslavpepmhopcqdabhmqsoqxjswitkwzkoefhfydeartdhreiyzgummxpbtmrxcogmtwjrhdejprotvhzebdvrbedsieznynuaxqcvuegtefvxltovozpqjqocqvnxkesbewmfeacmrmgehyvrfksbbctcmxnbqnlvogjjgzotghxdrpdzyyrdbpvgusyreehfkqxzcgdekjtahubwvcuiktwdczjxacwuqxrtbhjsoqmbqorihykbzcxlyteoourrhheveamoidfxqudkzrpfftcpropwjeymetuibsdatmbvlmjghexejvplaysxbguijitfvrlkgayprkljshhvlonydoxbcuvbwacyeuvzfqqzmanfioyrybcdhkvlizdagpskdcaloglhluokblzgsppcbj"))
print(s.longestPalindromeMethod3('gjjg'))