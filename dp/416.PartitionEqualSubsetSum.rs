struct Solution;

impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let N = nums.len();
        let total: i32 = nums.iter().sum();
        if total % 2 != 0 {
            return false;
        }
        let target = total / 2;

        let mut dp = vec![vec![false; N + 1]; (target + 1) as usize];

        for i in 1..=N {
            dp[0][i] = true;
        }

        for j in 1..=target {
            dp[j as usize][0] = false;
        }

        dp[0][0] = true;

        for sum in 1..=target {
            for idx in 1..=N {
                let num = nums[idx - 1];
                let left = dp[sum as usize][idx - 1];
                dp[sum as usize][idx] = left;
                if sum >= num && left == false {
                    let diff = (sum - num) as usize;
                    dp[sum as usize][idx] = dp[diff][idx - 1];
                }
            }
        }

        dp[target as usize][N]
    }
}
fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::can_partition(vec![1, 5, 11, 5]), true);
        assert_eq!(Solution::can_partition(vec![1, 2, 3, 5]), false);
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::can_partition(vec![1]), false);
        assert_eq!(Solution::can_partition(vec![2]), false);
        assert_eq!(Solution::can_partition(vec![1, 3]), false);
        assert_eq!(Solution::can_partition(vec![2, 2]), true);
        assert_eq!(Solution::can_partition(vec![1, 3, 2]), true);
        assert_eq!(Solution::can_partition(vec![1, 2, 3]), true);
        assert_eq!(Solution::can_partition(vec![2, 2, 2]), false);
        assert_eq!(Solution::can_partition(vec![3, 3, 3, 1]), false);
        assert_eq!(Solution::can_partition(vec![2, 2, 1, 1]), true);
    }

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
