struct Solution;

use std::cmp;

impl Solution {
    fn find_max(arr: &[i32]) -> i32 {
        *arr.iter().max().unwrap()
    }

    pub fn _trap1(height: Vec<i32>) -> i32 {
        // brute force
        let mut result: i32 = 0;
        let length = height.len();

        for i in 0..length {
            let left_max = Solution::find_max(&height[..=i]); // includes ith
            let right_max = Solution::find_max(&height[i..]);
            let water = cmp::min(left_max, right_max) - height[i];
            result = result + water;
        }

        result
    }

    pub fn trap2(height: Vec<i32>) -> i32 {
        let length = height.len();
        if length == 1 {
            return 0;
        }

        let mut result: i32 = 0;
        let mut left_max: Vec<i32> = vec![0; length];
        let mut right_max: Vec<i32> = vec![0; length];

        left_max[0] = height[0];
        for i in 1..=length - 1 {
            left_max[i] = cmp::max(height[i], left_max[i - 1]);
        }

        right_max[length - 1] = height[length - 1];
        for i in (0..=length - 2).rev() {
            right_max[i] = cmp::max(height[i], right_max[i + 1]);
        }

        for i in 0..length {
            let water = cmp::min(left_max[i], right_max[i]) - height[i];
            result = result + water;
        }

        result
    }

    pub fn trap(height: Vec<i32>) -> i32 {
        let length = height.len();
        if length == 1 {
            return 0;
        }

        let mut result = 0;
        let (mut left_max, mut right_max) = (0, 0);
        let (mut left, mut right) = (0, length - 1);

        loop {
            if left > right {
                break;
            }

            if left_max < right_max {
                if height[left] > left_max {
                    left_max = height[left];
                } else {
                    result += left_max - height[left];
                }
                left += 1;
            } else {
                if height[right] > right_max {
                    right_max = height[right];
                } else {
                    result += right_max - height[right];
                }
                right -= 1;
            }
        }

        result
    }
}

fn main() {
    assert_eq!(Solution::trap(vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6);
    assert_eq!(Solution::trap(vec![4, 2, 0, 3, 2, 5]), 9);
    assert_eq!(Solution::trap(vec![1, 1, 1, 1, 1]), 0);
    assert_eq!(Solution::trap(vec![1, 2, 3, 4, 3, 2, 1]), 0);
    assert_eq!(Solution::trap(vec![5, 4, 3, 4, 5]), 4);
    assert_eq!(Solution::trap(vec![0]), 0);
    assert_eq!(Solution::trap(vec![0, 1]), 0);
    assert_eq!(Solution::trap(vec![2, 1]), 0);
    assert_eq!(Solution::trap(vec![2, 1, 2]), 1);
    assert_eq!(Solution::trap(vec![2, 3, 2]), 0);
}
