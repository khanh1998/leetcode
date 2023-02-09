struct Solution;

impl Solution {
    pub fn count_and_say(n: i32) -> String {
        let mut curr = String::from("1");
        let mut i = 1;
        while i < n {
            i += 1;
            let mut next = String::new();
            let mut point = 0;
            for (idx, ch1) in curr.chars().enumerate() {
                if let Some(ch2) = curr.chars().nth(idx + 1) {
                    if !ch1.eq(&ch2) {
                        let count = idx - point + 1;
                        point = idx + 1;
                        next.push(char::from_digit(count as u32, 10).unwrap());
                        next.push(ch1);
                    }
                } else {
                    // end of string
                    let count = idx - point + 1;
                    next.push(char::from_digit(count as u32, 10).unwrap());
                    next.push(ch1);
                }
            }
            curr = next;
        }
        curr
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::count_and_say(1), "1".to_string());
        assert_eq!(Solution::count_and_say(2), "11".to_string());
        assert_eq!(Solution::count_and_say(3), "21".to_string());
        assert_eq!(Solution::count_and_say(4), "1211".to_string());
        assert_eq!(Solution::count_and_say(5), "111221".to_string());
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
