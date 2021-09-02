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



s = Solution()
print(s.longestPalindrome("rfvtmdqjppztlvotnstyqeildrnevqkcoiqndxxncftlhdychrutvzkcxjnduhssfiatzisxioyuqmxqpdiouixfhyjlnfsjupwjztuyklrweuqmkuygndrqfhhcxrxcwdwcwgsknxxmxiwqxjbbljnckdgofehoarikioabmisfuzraxcaryjzsjetrvvpavbhbajrsnvrfjorjzpcjmkoekaipinfzhuaegaxzzvlwclbzhqzbtvxtgfhojqhcnokzqbedusoywsfsgbwxbvrqgmzojdmhlmzwtcvvmhnytqqlkpwyesbztabhyfukhpbchhvtzoegykvbzrywjcntrmsyokklsnzwkpjdcdcayfauuxcydiubnonpumcogiwqsqzagxhwbvkcxojfvewzqjdbbwbudxndyvubbumrktckrgxtbanatsfsxtckueqqtldfnxeznozegxnzntynlfavlmdfgpwgebylkromwrwxflgylbrtbyjblvgrxlkuhwnjmzqkngdghjvrsgtppkgsmpxrsahxlakadliwxmnbztfadwoglocbvwvhgcmgnkdtlbnqbfepbupfticejjxjoogutfvckdvztgjuklczwiimstpstbreffkvcmvofanuxndahhftbvsbfgoagwptvszptjatyoemevxnpqxboiycubeoqfenopwcbzbfnqtixtqrpzatq"))