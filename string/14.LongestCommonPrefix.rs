struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut i = 0;
        loop {
            let mut c1: char;
            match strs[0].chars().nth(i) {
                Some(v) => c1 = v,
                None => break,
            }

            let mut stop = false;
            for s in strs.iter() {
                if let Some(c2) = s.chars().nth(i) {
                    if c2 != c1 {
                        stop = true;
                        break;
                    }
                } else {
                    stop = true;
                    break;
                }
            }
            if stop {
                break;
            } else {
                i += 1;
            }
        }
        strs[0][..i].to_string()
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
            Solution::longest_common_prefix(
                vec!["flower", "flow", "flight"]
                    .iter()
                    .map(|s| s.to_string())
                    .collect(),
            ),
            "fl"
        );
        assert_eq!(
            Solution::longest_common_prefix(
                vec!["dog", "racecar", "car"]
                    .iter()
                    .map(|s| s.to_string())
                    .collect(),
            ),
            ""
        );
        assert_eq!(
            Solution::longest_common_prefix(
                vec!["dog", "date", "day"]
                    .iter()
                    .map(|s| s.to_string())
                    .collect(),
            ),
            "d"
        );
        assert_eq!(
            Solution::longest_common_prefix(
                vec!["dog", "dog", "dog"]
                    .iter()
                    .map(|s| s.to_string())
                    .collect(),
            ),
            "dog"
        );
        assert_eq!(
            Solution::longest_common_prefix(
                vec!["damage"]
                    .iter()
                    .map(|s| s.to_string())
                    .collect(),
            ),
            "damage"
        );
    }

    #[test]
    fn test2() {}

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
