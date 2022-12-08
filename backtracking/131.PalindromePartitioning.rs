use std::vec;

struct Solution;

impl Solution {
    // build a matrix to check if any substring is panlindrome or not.
    pub fn build_matrix(s: &str) -> Vec<Vec<bool>> {
        let length = s.len();
        let mut matrix = vec![vec![false; length]; length];
        let chars = s.as_bytes(); // because all characters in string are ASCII

        // base case
        // sub string length = 1
        for start in 0..length {
            matrix[start][start] = true;
        }
        // sub string length = 2
        for start in 0..length - 1 {
            if chars[start] == chars[start + 1] {
                matrix[start][start + 1] = true;
            }
        }

        // regular case
        for spaces in 2..length {
            // space beween characters, sub_len = 3, means two spaces -> the sub string has 3 characters
            for start in 0..length - spaces {
                let end = start + spaces;
                if chars[start] == chars[end] {
                    matrix[start][end] = matrix[start + 1][end - 1]
                }
            }
        }
        matrix
    }

    pub fn calc(
        check: &Vec<Vec<bool>>,
        s: &str,
        start_idx: usize,
        path: &mut Vec<String>,
    ) -> Vec<Vec<String>> {
        let mut result: Vec<Vec<String>> = Vec::new();
        let length = s.len();
        if start_idx >= length {
            return vec![path.clone()];
        }

        for i in start_idx..length {
            if check[start_idx][i] {
                path.push(s[start_idx..=i].to_string());

                let res = &mut Solution::calc(check, s, i + 1, path);
                result.append(res);

                path.pop();
            }
        }

        result
    }

    pub fn partition(s: String) -> Vec<Vec<String>> {
        let check = &Solution::build_matrix(&s);
        let path: &mut Vec<String> = &mut Vec::new();
        Solution::calc(check, &s, 0, path)
    }
}
fn main() {
    let length = 5;
    let matrix = vec![vec![false; length]; length];
    println!("{:#?}", matrix);
}

#[cfg(test)]
mod tests {
    use crate::Solution;
    #[test]
    fn test_partition() {
        println!("{:#?}", Solution::partition("aabcc".to_string()));
        println!("{:#?}", Solution::partition("aab".to_string()));
        println!("{:#?}", Solution::partition("a".to_string()));

    }

    #[test]
    fn test_build_matrix_3() {
        let res = Solution::build_matrix("aba");
        let expected = [
            [true, false, true],
            [false, true, false],
            [false, false, true],
        ];
        assert_eq!(res, expected);

        let res = Solution::build_matrix("aaa");
        let expected = [
            [true, true, true],
            [false, true, true],
            [false, false, true],
        ];
        assert_eq!(res, expected);

        let res = Solution::build_matrix("abc");
        let expected = [
            [true, false, false],
            [false, true, false],
            [false, false, true],
        ];
        assert_eq!(res, expected);

        let res = Solution::build_matrix("abb");
        let expected = [
            [true, false, false],
            [false, true, true],
            [false, false, true],
        ];
        assert_eq!(res, expected);
    }

    #[test]
    fn test_build_matrix_2() {
        let res = Solution::build_matrix("aa");
        let expected = [[true, true], [false, true]];
        assert_eq!(res, expected);

        let res = Solution::build_matrix("ab");
        let expected = [[true, false], [false, true]];
        assert_eq!(res, expected);
    }

    #[test]
    fn test_build_matrix_1() {
        let res = Solution::build_matrix("a");
        let expected = [[true]];
        assert_eq!(res, expected)
    }

    #[test]
    fn test_build_matrix_5() {
        let res = Solution::build_matrix("abcba");
        let expected = [
            [true, false, false, false, true],
            [false, true, false, true, false],
            [false, false, true, false, false],
            [false, false, false, true, false],
            [false, false, false, false, true],
        ];
        assert_eq!(res, expected)
    }
}
