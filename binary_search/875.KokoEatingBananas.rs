struct Solution;
impl Solution {
    pub fn calc_time(piles: &Vec<i32>, speed: u64) -> u64 {
        let mut total_hours = 0;
        for pile in piles {
            total_hours += (*pile as f64/ speed as f64).ceil() as u64;
        }
        total_hours
    }
    pub fn min_eating_speed(piles: Vec<i32>, hours: i32) -> i32 {
        let max_speed = *piles.iter().max().unwrap();
        if (hours as usize) == piles.len() {
            return max_speed;
        }

        let mut target_time = hours as u64;
        let mut min_speed = max_speed;
        let (mut left, mut right) = (1 as u64, max_speed as u64);

        loop {
            if left > right {
                break;
            }

            let current_speed = (right + left) / 2;

            let current_time = Solution::calc_time(&piles, current_speed);

            println!("left={left} right={right}");
            println!("current speed={current_speed} current time={current_time} min speed={min_speed} target time={target_time}");

            if current_time > target_time {
                // too slow, increase speed
                left = current_speed + 1;
            } else if current_time <= target_time {
                min_speed = current_speed as i32;
                // too fast, decrease speed
                right = current_speed - 1;
            }
            println!("left={left} right={right}");
            println!("-----------")
        }

        min_speed
    }
}
fn main() {
    let a = 2.000000064_f64;
    let res = 1000000000 as f64 / a;
    println!("{}", res.ceil());
}

#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn search_for_row() {
        assert_eq!(Solution::min_eating_speed(vec![805306368,805306368,805306368], 1000000000), 3);
        assert_eq!(Solution::min_eating_speed(vec![1000000000], 2), 500000000);
        assert_eq!(Solution::min_eating_speed(vec![3], 8), 1);
        assert_eq!(Solution::min_eating_speed(vec![3, 6, 7, 11], 8), 4);
        assert_eq!(Solution::min_eating_speed(vec![3, 6, 7, 11], 4), 11);
        assert_eq!(Solution::min_eating_speed(vec![30, 11, 23, 4, 20], 5), 30);
        assert_eq!(Solution::min_eating_speed(vec![30, 11, 23, 4, 20], 6), 23);
    }
}
