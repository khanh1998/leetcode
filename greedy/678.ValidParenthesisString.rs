use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut stack: Vec<usize> = vec![];
        let mut asterisk_stack: Vec<usize> = vec![];

        if s.chars().last().unwrap() == '(' {
            return false;
        }

        for (index, ch) in s.chars().enumerate() {
            if ch == '(' {
                stack.push(index);
            }

            if ch == '*' {
                asterisk_stack.push(index);
            }

            if ch == ')' {
                if let None = stack.pop() {
                    if let None = asterisk_stack.pop() {
                        return false;
                    }
                }
            }
        }

        if asterisk_stack.len() < stack.len() {
            return false;
        }

        while stack.len() > 0 {
            let ch_idx = stack.pop().unwrap();
            let asterisk_idx = asterisk_stack.pop().unwrap();
            if ch_idx > asterisk_idx {
                return false;
            }
        }

        true
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::check_valid_string("()".to_string()), true);
        assert_eq!(Solution::check_valid_string("(*)".to_string()), true);
        assert_eq!(Solution::check_valid_string("(*))".to_string()), true);
        assert_eq!(Solution::check_valid_string("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())".to_string()), false);
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::check_valid_string("(".to_string()), false);
        assert_eq!(Solution::check_valid_string(")".to_string()), false);
        assert_eq!(Solution::check_valid_string("*".to_string()), true);
    }

    #[test]
    fn test3() {
        assert_eq!(Solution::check_valid_string("(*".to_string()), true);
        assert_eq!(Solution::check_valid_string(")*".to_string()), false);
        assert_eq!(Solution::check_valid_string("*)".to_string()), true);
        assert_eq!(Solution::check_valid_string("*(".to_string()), false);
        assert_eq!(Solution::check_valid_string("**".to_string()), true);
    }

    #[test]
    fn test4() {
        assert_eq!(Solution::check_valid_string("***".to_string()), true);

        assert_eq!(Solution::check_valid_string("(**".to_string()), true);
        assert_eq!(Solution::check_valid_string(")**".to_string()), false);
        assert_eq!(Solution::check_valid_string("*(*".to_string()), true);
        assert_eq!(Solution::check_valid_string("*)*".to_string()), true);
        assert_eq!(Solution::check_valid_string("**(".to_string()), false);
        assert_eq!(Solution::check_valid_string("**)".to_string()), true);

        assert_eq!(Solution::check_valid_string("((*".to_string()), false);
        assert_eq!(Solution::check_valid_string("()*".to_string()), true);
        assert_eq!(Solution::check_valid_string("))*".to_string()), false);
        assert_eq!(Solution::check_valid_string(")(*".to_string()), false);

        assert_eq!(Solution::check_valid_string("*((".to_string()), false);
        assert_eq!(Solution::check_valid_string("*()".to_string()), true);
        assert_eq!(Solution::check_valid_string("*))".to_string()), false);
        assert_eq!(Solution::check_valid_string("*)(".to_string()), false);

        assert_eq!(Solution::check_valid_string("(*(".to_string()), false);
        assert_eq!(Solution::check_valid_string("(*)".to_string()), true);
        assert_eq!(Solution::check_valid_string(")*)".to_string()), false);
        assert_eq!(Solution::check_valid_string(")*(".to_string()), false);
    }

    #[test]
    fn test5() {}
}
