use std::collections::BinaryHeap;

struct Solution;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut heap: BinaryHeap<i32> = BinaryHeap::from(stones);

        loop {
            if heap.len() <= 1 {
                break;
            }

            let a = heap.pop().unwrap();
            let b = heap.pop().unwrap();
            let diff = (a - b).abs();
            if diff > 0 {
                heap.push(diff);
            }
        }

        return heap.pop().or(Some(0)).unwrap();
    }
}
