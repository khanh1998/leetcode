use std::ops::Add;

struct Solution;

impl Solution {
    fn add_two_nums(mut num1: String, mut num2: String) -> String {
        let mut result = String::new();

        if num1.len() > num2.len() {
            let quantity = (num1.len() - num2.len()) as i32;
            num2 = Solution::pad_zeros(num2, quantity, true);
        }
        if num2.len() > num1.len() {
            let quantity = (num2.len() - num1.len()) as i32;
            num1 = Solution::pad_zeros(num1, quantity, true);
        }

        let mut carry = 0;

        let mut iter1 = num1.chars().rev();
        let mut iter2 = num2.chars().rev();

        loop {
            let d1 = iter1.next();
            let d2 = iter2.next();
            if d1 == None || d2 == None {
                break;
            }

            let sum = d1.unwrap().to_digit(10).unwrap() + d2.unwrap().to_digit(10).unwrap() + carry;
            let d = sum % 10;
            carry = sum / 10;

            result = d.to_string().add(&result);
        }

        if carry > 0 {
            result = carry.to_string().add(&result);
        }

        result
    }

    fn pad_zeros(num: String, quantity: i32, left: bool) -> String {
        let mut zero_str = String::new();
        for _ in 0..quantity {
            zero_str.push('0');
        }

        if left {
            return zero_str.add(&num);
        }

        num.add(&zero_str)
    }

    fn remove_leading_zero(num: String) -> String {
        let mut pointer = 0;
        let mut iter = num.chars();

        while iter.next() == Some('0') {
            pointer += 1;
        }

        if pointer >= num.len() {
            // all digits are zero
            return "0".to_string();
        }

        num[pointer..].to_string()
    }

    fn multiply_digit(num: &str, digit: u32) -> String {
        let mut result = String::new();
        let mut carry = 0;
        for d in num.chars().rev() {
            let tmp = d.to_digit(10).unwrap() * digit + carry;
            let mut new_d = tmp % 10;
            carry = tmp / 10;
            result = new_d.to_string().add(&result);
        }
        if carry > 0 {
            result = carry.to_string().add(&result);
        }
        result
    }

    pub fn multiply(num1: String, num2: String) -> String {
        let mut result = String::from("0");

        for (index, ch) in num2.chars().rev().enumerate() {
            let digit = ch.to_digit(10).unwrap();
            let mul = Solution::multiply_digit(&num1, digit);
            let padded = Solution::pad_zeros(mul, index as i32, false);
            result = Solution::add_two_nums(result, padded);
        }

        Solution::remove_leading_zero(result)
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::multiply_digit(&"23", 5), "115".to_string());
        assert_eq!(Solution::multiply_digit(&"23", 0), "00".to_string());
    }

    #[test]
    fn test2() {
        assert_eq!(
            Solution::remove_leading_zero("0".to_string()),
            "0".to_string()
        );
        assert_eq!(
            Solution::remove_leading_zero("00".to_string()),
            "0".to_string()
        );
        assert_eq!(
            Solution::remove_leading_zero("000".to_string()),
            "0".to_string()
        );
        assert_eq!(
            Solution::remove_leading_zero("001".to_string()),
            "1".to_string()
        );
        assert_eq!(
            Solution::remove_leading_zero("021".to_string()),
            "21".to_string()
        );
        assert_eq!(
            Solution::remove_leading_zero("201".to_string()),
            "201".to_string()
        );
        assert_eq!(
            Solution::remove_leading_zero("2010".to_string()),
            "2010".to_string()
        );
    }

    #[test]
    fn test3() {
        assert_eq!(
            Solution::add_two_nums("1".to_string(), "2".to_string()),
            "3".to_string()
        );
        assert_eq!(
            Solution::add_two_nums("1".to_string(), "2".to_string()),
            "3".to_string()
        );
        assert_eq!(
            Solution::add_two_nums("0".to_string(), "2".to_string()),
            "2".to_string()
        );
        assert_eq!(
            Solution::add_two_nums("4".to_string(), "0".to_string()),
            "4".to_string()
        );
        assert_eq!(
            Solution::add_two_nums("9".to_string(), "1".to_string()),
            "10".to_string()
        );
        assert_eq!(
            Solution::add_two_nums("9".to_string(), "9".to_string()),
            "18".to_string()
        );
    }

    #[test]
    fn test4() {
        assert_eq!(
            Solution::pad_zeros("1".to_string(), 1, true),
            "01".to_string()
        );
        assert_eq!(
            Solution::pad_zeros("1".to_string(), 1, false),
            "10".to_string()
        );
    }

    #[test]
    fn test5() {
        assert_eq!(
            Solution::multiply("2".to_string(), "3".to_string()),
            "6".to_string()
        );
        assert_eq!(
            Solution::multiply("20".to_string(), "3".to_string()),
            "60".to_string()
        );
        assert_eq!(
            Solution::multiply("200".to_string(), "11".to_string()),
            "2200".to_string()
        );
        assert_eq!(
            Solution::multiply("0".to_string(), "12345".to_string()),
            "0".to_string()
        );
        assert_eq!(
            Solution::multiply("1".to_string(), "12345".to_string()),
            "12345".to_string()
        );
    }
}
