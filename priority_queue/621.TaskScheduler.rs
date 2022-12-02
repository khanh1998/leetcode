struct Solution;

use std::collections::{BinaryHeap, HashMap, VecDeque};

impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let n: u32 = n as u32;
        let mut map: HashMap<char, u32> = HashMap::new();
        let mut queue: VecDeque<(u32, u32)> = VecDeque::new();
        let mut heap: BinaryHeap<u32> = BinaryHeap::new();

        for task in tasks {
            let count = map.entry(task).or_insert(0);
            *count += 1;
        }

        for count in map.values() {
            heap.push(*count);
        }

        let mut current_time = 1;

        loop {
            // pop from queue to heap
            let mut pop_front = false;

            if let Some((_, time)) = queue.get(0) {
                if *time <= current_time {
                    pop_front = true;
                }
            }

            if pop_front {
                if let Some((count, _)) = queue.pop_front() {
                    heap.push(count);
                }
            }

            // pop from heap, might put back to queue

            if let Some(count) = heap.pop() {
                let new_count = count - 1;
                let ready_time = current_time + n + 1;
                if new_count > 0 {
                    queue.push_back((new_count, ready_time));
                }
            }

            if queue.len() == 0 && heap.len() == 0 {
                break;
            }

            current_time += 1;
        }

        current_time as i32
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn default_test() {
        assert_eq!(
            Solution::least_interval(vec!['A', 'A', 'A', 'B', 'B', 'B'], 2),
            8
        );

        assert_eq!(
            Solution::least_interval(vec!['A', 'A', 'A', 'B', 'B', 'B'], 0),
            6
        );

        assert_eq!(
            Solution::least_interval(
                vec!['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
                2
            ),
            16
        );
    }
    struct TestCase {
        tasks: Vec<char>,
        n: i32,
        output: i32,
    }

    impl TestCase {
        fn new(tasks_str: &str, n: i32, output: i32) -> Self {
            let mut tasks: Vec<char> = Vec::new();

            for c in tasks_str.to_uppercase().chars() {
                tasks.push(c);
            }

            TestCase{tasks, n, output}
        }
    }

    #[test]
    fn my_test() {
        let mut test_cases: Vec<TestCase> = Vec::new();
        test_cases.push(TestCase::new("a", 0, 1));
        test_cases.push(TestCase::new("a", 2, 1));
        test_cases.push(TestCase::new("ab", 0, 2));
        test_cases.push(TestCase::new("ab", 1, 2));
        test_cases.push(TestCase::new("ab", 2, 2));
        test_cases.push(TestCase::new("aab", 0, 3));
        test_cases.push(TestCase::new("aab", 1, 3));
        test_cases.push(TestCase::new("aab", 2, 4));
        test_cases.push(TestCase::new("aabb", 0, 4));
        test_cases.push(TestCase::new("aabb", 1, 4));
        test_cases.push(TestCase::new("aabb", 2, 5));
        test_cases.push(TestCase::new("aabb", 3, 6));
        test_cases.push(TestCase::new("aaabbbccc", 0, 9));
        test_cases.push(TestCase::new("aaabbbccc", 1, 9));
        test_cases.push(TestCase::new("aaabbbccc", 2, 9));
        test_cases.push(TestCase::new("aaabbbccc", 3, 11));

        for (index, test) in test_cases.iter().enumerate() {
            assert_eq!(Solution::least_interval(test.tasks.clone(), test.n), test.output, "index={index}");
        }
    }
}
