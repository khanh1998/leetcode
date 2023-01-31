struct Solution;

impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = vec![];
        let mut carry = 1;
        for digit in digits.iter().rev() {
            let tmp = digit + carry;
            carry = tmp / 10;
            let new = tmp % 10;
            result.insert(0, new);
        }

        if carry > 0 {
            result.insert(0, carry);
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
        assert_eq!(Solution::plus_one(vec![0]), vec![1]);
        assert_eq!(Solution::plus_one(vec![1]), vec![2]);
        assert_eq!(Solution::plus_one(vec![2]), vec![3]);
        assert_eq!(Solution::plus_one(vec![9]), vec![1, 0]);
        assert_eq!(Solution::plus_one(vec![1, 9]), vec![2, 0]);
        assert_eq!(Solution::plus_one(vec![1, 0]), vec![1, 1]);
        assert_eq!(Solution::plus_one(vec![9, 9]), vec![1, 0, 0]);
    }
}
