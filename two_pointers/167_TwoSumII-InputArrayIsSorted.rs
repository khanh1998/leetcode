struct Solution;

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let (mut left, mut right) = (0, numbers.len() - 1);
        let mut result: Vec<i32> = Vec::with_capacity(2);

        loop {
            let sum = numbers[left] + numbers[right];

            if sum < target {
                left = left + 1;
            }
            if sum > target {
                right = right - 1;
            }
            if sum == target {
                result.push((left + 1) as i32);
                result.push((right + 1) as i32);
                break;
            }
        }

        result
    }
}

fn main() {
    assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), vec![1, 2]);
    assert_eq!(Solution::two_sum(vec![2, 3, 4], 6), vec![1, 3]);
    assert_eq!(Solution::two_sum(vec![-1, 0], -1), vec![1, 2]);
}