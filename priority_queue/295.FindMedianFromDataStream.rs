use std::{collections::BinaryHeap, cmp::Reverse};

struct MedianFinder {
    max_heap: BinaryHeap<i32>,
    min_heap: BinaryHeap<Reverse<i32>>,
}

impl MedianFinder {
    fn new() -> Self {
        MedianFinder {
            max_heap: BinaryHeap::new(),
            min_heap: BinaryHeap::new(),
        }
    }

    fn add_num(&mut self, num: i32) {
        self.max_heap.push(num);
        let neg_num = Reverse(self.max_heap.pop().unwrap());
        self.min_heap.push(neg_num);
        if self.min_heap.len() > self.max_heap.len() {
            let Reverse(neg_num) = self.min_heap.pop().unwrap();
            self.max_heap.push(neg_num)
        }
    }

    fn find_median(&self) -> f64 {
        // constraint: at least one num is inputted
        if self.max_heap.len() > self.min_heap.len() {
            return *self.max_heap.peek().unwrap() as f64;
        } else {
            let small = *self.max_heap.peek().unwrap() as f64;
            let Reverse(big) = self.min_heap.peek().unwrap();
            let res: f64 = (small + *big as f64) / 2.0;
            return res;
        }
    }
}
