struct Solution;

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let length = temperatures.len();
        let mut result: Vec<i32> = vec![0; length];
        let mut stack: Vec<(usize, i32)> = Vec::new();

        for (index, current_temp) in temperatures.iter().enumerate().rev() {
            loop {
                match stack.last() {
                    Some((_, warmer_candidate)) => {
                        if warmer_candidate <= current_temp {
                            stack.pop();
                        } else {
                            break;
                        }
                    }
                    None => {
                        break;
                    }
                };
            }

            if stack.len() == 0 {
                result[index] = 0;
            } else {
                let (warmer_index, _) = stack.last().unwrap();
                result[index] = (*warmer_index - index) as i32;
            }
            stack.push((index, *current_temp));
        }
        result
    }
}
fn main() {
    assert_eq!(
        Solution::daily_temperatures(vec![73, 74, 75, 71, 69, 72, 76, 73]),
        vec![1, 1, 4, 2, 1, 1, 0, 0]
    );
    assert_eq!(
        Solution::daily_temperatures(vec![30, 40, 50, 60]),
        vec![1, 1, 1, 0]
    );
    assert_eq!(
        Solution::daily_temperatures(vec![30, 60, 90]),
        vec![1, 1, 0]
    );
    assert_eq!(Solution::daily_temperatures(vec![30]), vec![0]);
    assert_eq!(Solution::daily_temperatures(vec![30,30]), vec![0, 0]);
    assert_eq!(Solution::daily_temperatures(vec![30,40]), vec![1, 0]);
    assert_eq!(Solution::daily_temperatures(vec![40,30]), vec![0, 0]);
}
