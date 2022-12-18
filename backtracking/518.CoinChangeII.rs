struct Solution;

impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        let coin_len = coins.len();
        let mut dp = vec![vec![0; coin_len + 1]; (amount + 1) as usize];
        for i in 1..=coin_len {
            dp[0][i] = 1;
        }

        for j in 1..=amount {
            dp[j as usize][0] = 0;
        }

        dp[0][0] = 1;

        for sub_amount in 1..=amount as usize {
            for num_coin in 1..=coin_len {
                let coin_val = coins[num_coin - 1] as usize;
                if sub_amount >= coin_val {
                    dp[sub_amount][num_coin] =
                        dp[sub_amount][num_coin - 1] + dp[sub_amount - coin_val][num_coin];
                } else {
                    dp[sub_amount][num_coin] = dp[sub_amount][num_coin - 1];
                }
            }
        }

        dp[amount as usize][coin_len]
    }
}
fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::change(5, vec![1, 2, 5]), 4);
        assert_eq!(Solution::change(3, vec![2]), 0);
        assert_eq!(Solution::change(10, vec![10]), 1);
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::change(10, vec![3, 8]), 0);
        assert_eq!(Solution::change(0, vec![3, 8]), 1);
        assert_eq!(Solution::change(0, vec![3]), 1);
    }

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
