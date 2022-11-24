struct Solution;

struct Item {
    position: i32,
    needed_time: f32, // to reach the target
}

impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let length = position.len();
        if length == 1 {
            return 1;
        }

        let mut items: Vec<Item> = vec![];
        for i in 0..length {
            let needed_time = (target - position[i]) as f32 / speed[i] as f32;
            let item = Item { position: position[i], needed_time };
            items.push(item);
        }

        items.sort_by_key(|item| item.position);

        let mut result: i32 = 0;
        let mut left = (length - 2) as i32;
        let mut right = (length - 1) as i32;

        loop {
            if left < 0 || right < 0 {
                result += 1;
                break;
            }

            if items[left as usize].needed_time <= items[right as usize].needed_time {
                left -= 1;
            } else {
                result += 1;
                right = left;
                left -= 1;
            }
        }

        result
    }
}

fn main() {
    assert_eq!(Solution::car_fleet(12, vec![10,8,0,5,3], vec![2,4,1,1,3]), 3);
    assert_eq!(Solution::car_fleet(10, vec![3], vec![3]), 1);
    assert_eq!(Solution::car_fleet(100, vec![25, 50], vec![50, 25]), 1);
    assert_eq!(Solution::car_fleet(100, vec![25, 50], vec![20, 25]), 2);
    assert_eq!(Solution::car_fleet(100, vec![0,2,4], vec![4,2,1]), 1);
    assert_eq!(Solution::car_fleet(100, vec![0,2,4], vec![4,2,5]), 2);
    assert_eq!(Solution::car_fleet(100, vec![0,2,4], vec![4,8,6]), 2);
    assert_eq!(Solution::car_fleet(100, vec![0,2,4], vec![1,2,3]), 3);
}
