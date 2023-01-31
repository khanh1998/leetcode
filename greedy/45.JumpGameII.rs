struct Solution;

impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let vec_len = nums.len();
        let mut left: usize = 0;
        let mut right: usize = 0;
        let mut count = 0;

        loop {
            if right >= vec_len - 1 {
                break;
            } else {
                count += 1;
            }

            // move to next left-to-right range.
            let new_left = right + 1;
            for i in left..=right {
                right = std::cmp::max(right, i + nums[i] as usize);
            }
            left = new_left;
        }

        count
    }
}

fn main() {
    let a = vec![2, 3, 1, 1, 4];
    println!("{:#?}", &a[0..=0])
}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::jump(vec![2, 3, 1, 1, 4]), 2);
        assert_eq!(Solution::jump(vec![2, 3, 0, 1, 4]), 2);
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::jump(vec![4]), 0);
        assert_eq!(Solution::jump(vec![1, 2]), 1);
        assert_eq!(Solution::jump(vec![1, 0]), 1);
        assert_eq!(Solution::jump(vec![1, 1, 1]), 2);
        assert_eq!(Solution::jump(vec![2, 1, 0]), 1);
        assert_eq!(Solution::jump(vec![2, 0, 0]), 1);
        assert_eq!(Solution::jump(vec![1, 1, 1, 1]), 3);
        assert_eq!(Solution::jump(vec![1, 2, 1, 1]), 2);
        assert_eq!(Solution::jump(vec![2, 1, 1, 1]), 2);
        assert_eq!(Solution::jump(vec![3, 2, 1, 1]), 1);
        assert_eq!(Solution::jump(vec![4, 3, 0, 1, 4]), 1);
        assert_eq!(Solution::jump(vec![1, 1, 1, 1, 4]), 4);
        assert_eq!(Solution::jump(vec![2, 1, 1, 1, 4]), 3);
        assert_eq!(Solution::jump(vec![1, 2, 1, 1, 4]), 3);
        assert_eq!(Solution::jump(vec![1, 1, 2, 1, 4]), 3);
    }

    #[test]
    fn test3() {
        assert_eq!(Solution::jump(vec![3, 4, 3, 2, 5, 4, 3]), 3);
    }

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
