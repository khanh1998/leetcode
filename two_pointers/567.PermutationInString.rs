struct Solution;

use std::{vec};

struct Counter {
    letter_2_counts: Vec<i32>,
    unique_letter_count: i32,
    total_letter_count: i32,

    tmp_letter_2_counts: Vec<i32>,
    tmp_unique_letter_count: i32,
    tmp_total_letter: i32,
}

impl Counter {
    fn new() -> Counter {
        Counter {
            letter_2_counts: vec![0; 26],
            unique_letter_count: 0,
            total_letter_count: 0,
            tmp_letter_2_counts: vec![0; 26],
            tmp_unique_letter_count: 0,
            tmp_total_letter: 0,
        }
    }

    fn log(&self) {
        println!("letter_2_counts={:#?}", self.letter_2_counts);
        println!("unique_letter_count={:#?}", self.unique_letter_count);
        println!("total_letter_count={:#?}", self.total_letter_count);
        println!("tmp_letter_2_counts={:#?}", self.tmp_letter_2_counts);
        println!(
            "tmp_unique_letter_count={:#?}",
            self.tmp_unique_letter_count
        );
        println!("tmp_total_letter={:#?}", self.tmp_total_letter);
    }

    fn init(&mut self, s1: &String) {
        self.total_letter_count = s1.len() as i32;

        for ch in s1.chars() {
            let index: usize = ch as usize - 97;

            self.letter_2_counts[index] += 1;
        }

        for i in 0..=25 {
            if self.letter_2_counts[i] > 0 {
                self.unique_letter_count += 1;
            }
        }

        self.log();
    }

    fn new_session(&mut self) {
        self.tmp_letter_2_counts = vec![0; 26];
        self.tmp_unique_letter_count = 0;
        self.tmp_total_letter = 0;
    }

    fn add(&mut self, ch: char) -> Result<(), ()> {
        let index = ch as usize - 97;
        if self.tmp_letter_2_counts[index] + 1 > self.letter_2_counts[index] {
            return Err(());
        }
        if self.tmp_letter_2_counts[index] + 1 == self.letter_2_counts[index] {
            self.tmp_unique_letter_count += 1;
        }

        self.tmp_letter_2_counts[index] += 1;
        self.tmp_total_letter += 1;

        Ok(())
    }

    fn remove(&mut self, ch: char) -> Result<(), ()> {
        let index = ch as usize - 97;
        if self.tmp_letter_2_counts[index] - 1 < 0 {
            return Err(());
        }
        if self.tmp_letter_2_counts[index] == self.letter_2_counts[index] {
            self.tmp_unique_letter_count -= 1;
        }

        self.tmp_letter_2_counts[index] -= 1;
        self.tmp_total_letter -= 1;

        Ok(())
    }

    fn is_matched(&self) -> bool {
        if self.tmp_unique_letter_count == self.unique_letter_count
            && self.tmp_total_letter == self.total_letter_count
        {
            return true;
        }
        false
    }
}

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let (mut left, mut right) = (0, 0);
        let mut counter = Counter::new();
        counter.init(&s1);
        counter.new_session();

        loop {
            println!("------------");
            if right >= s2.len() {
                break;
            }

            let right_ch = s2.chars().nth(right).unwrap();
            let add = counter.add(right_ch);
            println!("left={left} right={right}");
            println!("right={right_ch}");
            println!("add={:#?}", add);
            match add {
                Ok(_) => {
                    let matched = counter.is_matched();
                    println!("matched={matched}");
                    if matched {
                        return true;
                    }
                    right += 1;
                }
                Err(_) => {
                    if left < right {
                        let left_ch = s2.chars().nth(left).unwrap();
                        let remove = counter.remove(left_ch);
                        println!("left={left_ch}");
                        println!("remove={:#?}", remove);
                        match remove {
                            Ok(_) => {
                                left += 1;
                                if right < left {
                                    right = left
                                }
                            }
                            Err(_) => {
                                println!("something is wrong here");
                                break;
                            }
                        }
                    } else {
                        left += 1;
                        right = left;
                    }
                }
            }
        }

        false
    }
}

fn main() {
    assert_eq!(
        Solution::check_inclusion(String::from("ab"), String::from("eidbaooo")),
        true
    );
    assert_eq!(
        Solution::check_inclusion(String::from("ab"), String::from("eidboaoo")),
        false
    );
    assert_eq!(
        Solution::check_inclusion(String::from("a"), String::from("eidboaoo")),
        true
    );
    assert_eq!(
        Solution::check_inclusion(String::from("a"), String::from("a")),
        true
    );
    assert_eq!(
        Solution::check_inclusion(String::from("a"), String::from("b")),
        false
    );
    assert_eq!(
        Solution::check_inclusion(String::from("abcd"), String::from("dcba")),
        true
    );
    assert_eq!(
        Solution::check_inclusion(String::from("abcd"), String::from("abced")),
        false
    );
    assert_eq!(
        Solution::check_inclusion(String::from("abcd"), String::from("abc")),
        false
    );
}
