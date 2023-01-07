use std::{collections::HashMap};

struct Solution;

impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();
        let mut last_appear: HashMap<u8, usize> = HashMap::new();

        for (index, char) in s.bytes().enumerate() {
            last_appear.insert(char, index);
        }

        let length = s.len();
        let mut left = 0;

        let first_char = s.as_bytes().get(0).unwrap();
        let mut right = *last_appear.get(first_char).unwrap();

        let mut current = left;

        /*
            result = [1, 1]
            ab
            left = 2
            right = 1
            current = 1
            last appear = 0
        */

        loop {
            if current == right {
                result.push((right - left + 1) as i32);
                left = right + 1;
                current = left;

                if let Some(current_char) = s.as_bytes().get(current) {
                    right = *last_appear.get(current_char).unwrap();
                    continue;
                } else {
                    break;
                }
            }

            let current_char = s.as_bytes().get(current).unwrap();
            let last_app = *last_appear.get(current_char).unwrap();

            if right < last_app {
                right = last_app;
            }

            current += 1;
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
        assert_eq!(
            Solution::partition_labels("ababcbacadefegdehijhklij".to_string()),
            vec![9, 7, 8]
        );

        assert_eq!(
            Solution::partition_labels("eccbbbbdec".to_string()),
            vec![10]
        );
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::partition_labels("a".to_string()), vec![1]);
        assert_eq!(Solution::partition_labels("aa".to_string()), vec![2]);
        assert_eq!(Solution::partition_labels("aaa".to_string()), vec![3]);
        assert_eq!(Solution::partition_labels("aab".to_string()), vec![2, 1]);
        assert_eq!(Solution::partition_labels("abb".to_string()), vec![1, 2]);
        assert_eq!(Solution::partition_labels("abc".to_string()), vec![1, 1, 1]);
    }

    #[test]
    fn test3() {
        assert_eq!(Solution::partition_labels("ab".to_string()), vec![1, 1]);
    }

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
