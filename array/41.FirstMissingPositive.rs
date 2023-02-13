struct Solution;

impl Solution {
    pub fn swap(nums: &mut Vec<i32>, a: usize, b: usize) {
        if a < nums.len() && b < nums.len() {
            let tmp = nums[a];
            nums[a] = nums[b];
            nums[b] = tmp;
        }
    }

    pub fn is_valid_num(num: i32, length: usize) -> bool {
        return num > 0 && num < length as i32;
    }

    pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
        let mut i = 0;
        let length = nums.len();

        while i < length {
            let expected_num: i32 = i as i32 + 1;
            if !Solution::is_valid_num(nums[i], length) {
                i += 1;
                continue;
            }
            while Solution::is_valid_num(nums[i], length)
                && nums[i] != expected_num
                && nums[i] != nums[nums[i] as usize - 1]
            {
                let expected_idx = nums[i] as usize - 1;
                Solution::swap(&mut nums, i, expected_idx);
            }
            i += 1;
        }
        for i in 0..length {
            let expected_num = i as i32 + 1;
            if nums[i] != expected_num {
                return expected_num;
            }
        }
        length as i32 + 1
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(
            Solution::first_missing_positive(vec![-1, 4, 2, 1, 9, 10]),
            3
        );
        // -1, 4, 2, 1, 9, 10

        // -1, 1, 2, 4, 9, 10
        //  1,-1, 2, 4, 9, 1

        //  1, 2, -1, 4, 9, 10

        //  1, 2, -1, 4, 9, 10

        assert_eq!(Solution::first_missing_positive(vec![1, 2, 0]), 3);
        assert_eq!(Solution::first_missing_positive(vec![3, 4, -1, 1]), 2);
        assert_eq!(Solution::first_missing_positive(vec![7, 8, 9, 11, 12]), 1);
    }
}
