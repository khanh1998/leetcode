class Solution:
    def find(self, start_index: int) -> int:
        pass
    def numDecodings(self, s: str) -> int:
        # split the string into digits
        numbers = []
        i = 0
        while i < len(s):
            if i == len(s) - 1 or s[i + 1] != '0':
                numbers.append(int(s[i]))
                i += 1
            else:
                numbers.append(int(s[i] + '0'))
                i += 2
        print(numbers)
        # combine digits
        count = 1
        max_num_digit_pair = len(numbers) // 2
        for num_digit_pair in range(max_num_digit_pair):
            for i in range(len(numbers) - 1):
                sum = numbers[i] * 10 + numbers[i + 1]
                if sum <= 26 and numbers[i + 1] < 10:
                    count += 1
        print(count)
        return count


s = Solution()
s.numDecodings('11106')
