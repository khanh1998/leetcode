use std::{cmp, collections::VecDeque, num};

struct Solution;

impl Solution {
    pub fn max_product1(nums: Vec<i32>) -> i32 {
        let length = nums.len();
        let mut result = -2 * (10 ^ 5) - 1;
        let mut matrix = vec![vec![-1; length]; length];

        for i in 0..length {
            matrix[i][i] = *nums.get(i).unwrap();
            result = cmp::max(result, matrix[i][i]);
        }

        for size in 2..=length {
            for begin in 0..=length - size {
                let end = begin + size - 1;
                let div1 = (begin + end) / 2;
                let div2 = div1 + 1;
                let product = matrix[begin][div1] * matrix[div2][end];
                matrix[begin][end] = product;
                result = cmp::max(result, product);
            }
        }

        result
    }

    pub fn max_product2(nums: Vec<i32>) -> i32 {
        let mut result = *nums.iter().max().unwrap();
        let length = nums.len();
        let mut q = VecDeque::new();

        for (i, num) in nums.iter().enumerate() {
            let (begin, end) = (i, i);
            q.push_back((*num, begin, end));
        }

        while !q.is_empty() {
            let (product, begin, end) = q.pop_front().unwrap();
            if end + 1 < length {
                let new_product = product * nums[end + 1];
                result = cmp::max(new_product, result);
                q.push_back((new_product, begin, end + 1));
            }
        }
        
        result
    }

    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut result = -11;

        let mut cumulative = 1;
        for num in nums.iter() {
            cumulative *= num;
            result = cmp::max(result, cumulative);
            if cumulative == 0 {
                cumulative = 1;
            }
        }

        cumulative = 1;
        for num in nums.iter().rev() {
            cumulative *= *num;
            result = cmp::max(result, cumulative);
            if cumulative == 0 {
                cumulative = 1;
            }
        }

        result
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::max_product(vec![-2, 0, -1]), 0);
        assert_eq!(Solution::max_product(vec![2, 3, -2, 4]), 6);
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::max_product(vec![-2, 3, -2, 4]), 48);
        assert_eq!(Solution::max_product(vec![4]), 4);
        assert_eq!(Solution::max_product(vec![4, 2]), 8);
        assert_eq!(Solution::max_product(vec![4, 2, 3]), 24);
    }

    #[test]
    fn test3() {
        assert_eq!(Solution::max_product(vec![-4]), -4);
        assert_eq!(Solution::max_product(vec![4, -2]), 4);
        assert_eq!(Solution::max_product(vec![-4, -2]), 8);
        assert_eq!(Solution::max_product(vec![4, -2, 3]), 4);
        assert_eq!(Solution::max_product(vec![-4, -2, 3]), 24);
        assert_eq!(Solution::max_product(vec![4, -2, -3]), 24);
        assert_eq!(Solution::max_product(vec![-4, -2, -3]), 8);
    }

    #[test]
    fn test4() {
        assert_eq!(Solution::max_product(vec![-2, 3, -2, 4]), 48);
    }

    #[test]
    fn test5() {}
}
