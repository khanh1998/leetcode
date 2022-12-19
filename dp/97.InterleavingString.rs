struct Solution;

impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        let s1 = s1.as_bytes();
        let s2 = s2.as_bytes();
        let s3 = s3.as_bytes();

        let s1_len = s1.len();
        let s2_len = s2.len();

        if s1_len + s2_len != s3.len() {
            return false;
        }

        let mut dp = vec![vec![false; s2_len + 1]; s1_len + 1];

        // init data

        dp[0][0] = true;

        for i in 1..=s1_len {
            let k = i - 1;
            if s3[k] == s1[i - 1] {
                dp[i][0] = dp[i - 1][0];
            }
        }

        for j in 1..=s2_len {
            let k = j - 1;
            if s3[k] == s2[j - 1] {
                dp[0][j] = dp[0][j - 1];
            }
        }

        // process

        for row in 1..=s1_len {
            for col in 1..=s2_len {
                let k = row + col - 1;
                if s3[k] == s2[col - 1] && dp[row][col] == false {
                    dp[row][col] = dp[row][col - 1];
                }
                if s3[k] == s1[row - 1] && dp[row][col] == false {
                    dp[row][col] = dp[row - 1][col];
                }
            }
        }

        // for row in dp.iter() {
        //     for col in row.iter() {
        //         print!("{:5}, ", col);
        //     }
        //     println!()
        // }

        dp[s1_len][s2_len]
    }
}

fn main() {
    Solution::is_interleave(
        "aabcc".to_string(),
        "dbbca".to_string(),
        "aadbbcbcac".to_string(),
    );
}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(
            Solution::is_interleave(
                "aabcc".to_string(),
                "dbbca".to_string(),
                "aadbbcbcac".to_string()
            ),
            true
        );
        assert_eq!(
            Solution::is_interleave("abc".to_string(), "bcd".to_string(), "abcbdc".to_string()),
            true
        );
    }

    #[test]
    fn test2() {
        assert_eq!(
            Solution::is_interleave(
                "aabcc".to_string(),
                "dbbca".to_string(),
                "aadbbbaccc".to_string()
            ),
            false
        );
        assert_eq!(
            Solution::is_interleave("".to_string(), "".to_string(), "".to_string()),
            true
        );
    }

    #[test]
    fn test3() {
        assert_eq!(
            Solution::is_interleave("abcd".to_string(), "".to_string(), "abcd".to_string()),
            true
        );
        assert_eq!(
            Solution::is_interleave("".to_string(), "abcd".to_string(), "abcd".to_string()),
            true
        );
        assert_eq!(
            Solution::is_interleave("a".to_string(), "b".to_string(), "ba".to_string()),
            true
        );
        assert_eq!(
            Solution::is_interleave("a".to_string(), "b".to_string(), "ab".to_string()),
            true
        );
    }

    #[test]
    fn test4() {
        assert_eq!(
            Solution::is_interleave("ab".to_string(), "".to_string(), "ba".to_string()),
            false
        );
        assert_eq!(
            Solution::is_interleave("".to_string(), "".to_string(), "a".to_string()),
            false
        );
    }

    #[test]
    fn test5() {
        assert_eq!(
            Solution::is_interleave(
                "aabc".to_string(),
                "abad".to_string(),
                "aabadabc".to_string()
            ),
            true
        );
    }
}
