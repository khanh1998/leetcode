use std::collections::HashMap;

struct Solution;

impl Solution {
    fn memorize(
        nums: &Vec<i32>,
        index: usize,
        sum: i32,
        target: i32,
        cache: &mut HashMap<(usize, i32), i32>,
    ) -> i32 {
        if index == nums.len() {
            if sum == target {
                return 1;
            }
            return 0;
        }

        if cache.contains_key(&(index, sum)) {
            return *cache.get(&(index, sum)).unwrap();
        }

        let add = Solution::backtrack(nums, index + 1, sum + nums[index], target);
        let sub = Solution::backtrack(nums, index + 1, sum - nums[index], target);
        let result = add + sub;

        cache.insert((index, sum), result);

        result
    }

    fn backtrack(nums: &Vec<i32>, index: usize, sum: i32, target: i32) -> i32 {
        if index == nums.len() {
            if sum == target {
                return 1;
            }
            return 0;
        }
        let add = Solution::backtrack(nums, index + 1, sum + nums[index], target);
        let sub = Solution::backtrack(nums, index + 1, sum - nums[index], target);

        return add + sub;
    }

    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {
        // Solution::backtrack(&nums, 0, 0, target)
        let mut cache: HashMap<(usize, i32), i32> = HashMap::new();
        Solution::memorize(&nums, 0, 0, target, &mut cache)
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::find_target_sum_ways(vec![1, 1, 1, 1, 1], 3), 5);
        assert_eq!(Solution::find_target_sum_ways(vec![1], 1), 1);
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::find_target_sum_ways(vec![1], 0), 0);
        assert_eq!(Solution::find_target_sum_ways(vec![1], 2), 0);
        assert_eq!(Solution::find_target_sum_ways(vec![1, 2], 0), 0);
        assert_eq!(Solution::find_target_sum_ways(vec![1, 2], 1), 1);
        assert_eq!(Solution::find_target_sum_ways(vec![1, 2], 2), 0);
        assert_eq!(Solution::find_target_sum_ways(vec![1, 2], 3), 1);
        assert_eq!(Solution::find_target_sum_ways(vec![1, 2], 4), 0);
    }

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
