# https://leetcode.com/problems/longest-valid-parentheses/solution/
class Solution:
    def longestValidParenthesesDP(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        dp = [0] * (length)
        maxLength = 0
        for index in range(1, length):
            sublength = 0
            if s[index] == ')' and s[index - 1] == '(':
                sublength = dp[index - 2] + 2
            if s[index] == ')' and s[index - 1] == ')':
                openIndex = index - dp[index - 1] - 1
                if s[openIndex] == '(' and openIndex >= 0:
                    if openIndex == 0:
                        sublength = dp[index - 1] + 2
                    else:
                        sublength = dp[openIndex - 1] + dp[index - 1] + 2
            maxLength = max(sublength, maxLength)
            dp[index] = sublength
        print(dp)
        return maxLength

    def longestValidParentheses(self, s: str) -> int:
        print('------------------------')
        stack, res, s = [0], 0, ')'+s
        print(s)
        for i in range(1, len(s)):
            print(i, stack, s[stack[-1]], s[i])
            if s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
        return res

s = Solution()
print(s.longestValidParentheses('())') == 2)
#print(s.longestValidParentheses('((()') == 2)
print(s.longestValidParentheses(')()())') == 4)
print(s.longestValidParentheses('()(()))))') == 6)
print(s.longestValidParentheses('(()') == 2)
print(s.longestValidParentheses('') == 0)
print(s.longestValidParentheses('(()())') == 6)