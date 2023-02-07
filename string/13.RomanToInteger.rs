use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn subtraction(s: &[u8], i: usize) -> i32 {
        if let None = s.get(i + 1) {
            return 0;
        }
        let front = *s.get(i + 1).unwrap() as char;
        if let Some(behind) = s.get(i) {
            return match *behind as char {
                'I' => {
                    return match front {
                        'V' => 4,
                        'X' => 9,
                        _ => 0,
                    }
                }
                'X' => match front {
                    'L' => 40,
                    'C' => 90,
                    _ => 0,
                },
                'C' => match front {
                    'D' => 400,
                    'M' => 900,
                    _ => 0,
                },
                _ => 0,
            };
        }
        0
    }

    pub fn roman_to_int(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut i = 0;
        let mut result = 0;
        let mut map = HashMap::new();
        map.insert('I', 1);
        map.insert('V', 5);
        map.insert('X', 10);
        map.insert('L', 50);
        map.insert('C', 100);
        map.insert('D', 500);
        map.insert('M', 1000);
        while i < bytes.len() {
            let sub = Solution::subtraction(&bytes, i);
            if sub > 0 {
                result += sub;
                i += 2;
            } else {
                let c = bytes[i] as char;
                let add = *map.get(&c).unwrap();
                result += add;
                i += 1;
            }
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
        assert_eq!(Solution::roman_to_int("III".to_string()), 3);
        assert_eq!(Solution::roman_to_int("LVIII".to_string()), 58);
        assert_eq!(Solution::roman_to_int("MCMXCIV".to_string()), 1994);
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::roman_to_int("MCMXCVIII".to_string()), 1998);
        assert_eq!(Solution::roman_to_int("MCMXCIX".to_string()), 1999);
        assert_eq!(Solution::roman_to_int("MM".to_string()), 2000);
        assert_eq!(Solution::roman_to_int("MMI".to_string()), 2001);
        assert_eq!(Solution::roman_to_int("CDXLIV".to_string()), 444);
        assert_eq!(Solution::roman_to_int("CMXCIX".to_string()), 999);
    }

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
