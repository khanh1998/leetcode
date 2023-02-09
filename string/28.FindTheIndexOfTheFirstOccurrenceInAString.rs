struct Solution;

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle.len() > haystack.len() {
            return -1;
        }
        let end = haystack.len() - needle.len();
        let n_len = needle.len();

        for i in 0..=end {
            for j in 0..n_len {
                if needle.chars().nth(j) != haystack.chars().nth(i + j) {
                    break;
                }
                if j == n_len - 1 {
                    return i as i32;
                }
            }
        }
        -1
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
            Solution::str_str("sadbutsad".to_string(), "sad".to_string()),
            0
        );
        assert_eq!(
            Solution::str_str("leetcode".to_string(), "leeto".to_string()),
            -1
        );
    }

    #[test]
    fn test2() {
        assert_eq!(
            Solution::str_str("sabbutsad".to_string(), "sad".to_string()),
            6
        );
        assert_eq!(
            Solution::str_str("sabbutsad".to_string(), "but".to_string()),
            3
        );
        assert_eq!(
            Solution::str_str("sabbutsad".to_string(), "sabbutsad".to_string()),
            0
        );
        assert_eq!(
            Solution::str_str("sabbutsad".to_string(), "sabbutsa".to_string()),
            0
        );
        assert_eq!(
            Solution::str_str("sabbutsad".to_string(), "abbutsad".to_string()),
            1
        );
    }

    #[test]
    fn test3() {
        assert_eq!(Solution::str_str("abcdef".to_string(), "a".to_string()), 0);
        assert_eq!(Solution::str_str("abcdef".to_string(), "f".to_string()), 5);
        assert_eq!(Solution::str_str("abcdef".to_string(), "c".to_string()), 2);
    }

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
