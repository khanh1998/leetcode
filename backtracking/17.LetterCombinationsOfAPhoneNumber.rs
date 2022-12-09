use std::vec;

struct Solution;

impl Solution {
    pub fn calc(digit_to_letters: &Vec<Vec<char>>, digits: &str, index: usize, path: &mut String) -> Vec<String> {
        if index >= digits.len() {
            return vec![path.clone()];
        }

        let mut result: Vec<String> = Vec::new();

        if let Some(digit_char) = digits.as_bytes().get(index) {
            let digit = (digit_char - 48) as usize;
            if let Some(letters) = digit_to_letters.get(digit) {
                for letter in letters {
                    path.push(*letter);
                    let res = &mut Solution::calc(digit_to_letters, digits, index + 1, path);
                    result.append(res);
                    path.pop();
                }
            }
        }

        result
    }

    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.len() == 0 {
            return vec![]
        }
        
        let digit_to_letters = vec![
            vec![], // number 0
            vec![], // number 1
            vec!['a', 'b', 'c'],
            vec!['d', 'e', 'f'],
            vec!['g', 'h', 'i'],
            vec!['j', 'k', 'l'],
            vec!['m', 'n', 'o'],
            vec!['p', 'q', 'r', 's'],
            vec!['t', 'u', 'v'],
            vec!['w', 'x', 'y', 'z'],
        ];

        let mut path: String = String::new();

        Solution::calc(&digit_to_letters, &digits, 0, &mut path)
    }
}
fn main() {}

#[cfg(test)]
mod tests {
    use crate::Solution;
    #[test]
    fn test_partition() {
        let empty: Vec<String> = vec![];
        assert_eq!(Solution::letter_combinations("".to_string()), empty);
        assert_eq!(Solution::letter_combinations("2".to_string()), vec!["a", "b", "c"]);
        assert_eq!(Solution::letter_combinations("23".to_string()), vec!["ad","ae","af","bd","be","bf","cd","ce","cf"]);
    }
}
