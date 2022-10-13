from typing import List

MAX = 2 ** 31

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        coin_change = [0] + [MAX] * amount
        for current_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= current_amount:
                    notTake = coin_change[current_amount]
                    take = 1 + coin_change[current_amount-coin]
                    coin_change[current_amount] = min(take, notTake)
                else:
                    break

        if coin_change[-1] == MAX:
            return -1
        return coin_change[-1]

    def coinChange1(self, coins: List[int], amount: int) -> int:
        # time limit exceeded
        previous = [0] + [MAX] * amount # previous row of current row
        row = [0] + [MAX] * amount # relative current row
        
        for coin in coins:
            for current_amount in range(1, amount + 1):
                candidates = []
                max_coin_quantity = current_amount // coin
                for coin_quantity in range(max_coin_quantity + 1):
                    take_amount = coin_quantity * coin
                    base_amount = current_amount - take_amount
                    take = previous[base_amount] + coin_quantity # i = 0, means not to take
                    candidates.append(take)
                row[current_amount] = min(take, min(candidates))
            previous = list(row)
            row = [0] + [MAX] * amount
        if previous[-1] == MAX:
            return -1
        return previous[-1]

s = Solution()
print(s.coinChange([281,20,251,251], 7323))
print(s.coinChange([186,419,83,408], 6249) == 20)
print(s.coinChange([1,3,4,5], 7) == 2)
print(s.coinChange([2], 6) == 3)
print(s.coinChange([2], 3) == -1)
print(s.coinChange([1], 0) == 0)
print(s.coinChange([1,3], 10) == 4)
print(s.coinChange([4,3], 5) == -1)
print(s.coinChange([4,3], 0) == 0)
print(s.coinChange([1,2,5], 13) == 4)
print(s.coinChange([1,2,5], 11) == 3)
print(s.coinChange([4,2,5], 3) == -1)