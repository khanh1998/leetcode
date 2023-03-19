use std::{
    collections::{BinaryHeap, HashMap},
};

struct Solution;

impl Solution {
    pub fn compare_two_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> bool {
        let mut map = HashMap::new();
        for num in nums1 {
            let freq = map.entry(num).or_insert(0);
            *freq += 1;
        }

        for num in nums2 {
            if let Some(freq) = map.get_mut(&num) {
                *freq -= 1;
            } else {
                return false;
            }
        }

        for (_, freq) in map {
            if freq != 0 {
                return false;
            }
        }

        true
    }

    pub fn priority_queue(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut result = vec![];
        let mut num_freq: HashMap<i32, i32> = HashMap::new();
        let mut pq: BinaryHeap<(i32, i32)> = BinaryHeap::new();

        for num in nums {
            let freq = num_freq.entry(num).or_insert(0);
            *freq += 1;
        }

        for (num, freq) in num_freq {
            pq.push((freq, num));
        }

        for _ in 0..k {
            if let Some((_, num)) = pq.pop() {
                result.push(num);
            } else {
                break;
            }
        }

        result
    }

    pub fn swap(nums: &mut Vec<(i32, i32)>, a: usize, b: usize) {
        let tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }

    pub fn do_quick_select(
        nums: &mut Vec<(i32, i32)>,
        k: usize,
        begin: usize,
        end: usize,
    ) -> Vec<i32> {
        let mut left: i32 = begin as i32;
        let mut right: i32 = end as i32 - 1;
        let (_, pivot_freq) = nums[end];

        // descending order
        loop {
            while left <= right && nums.get(left as usize).unwrap().1 >= pivot_freq {
                left += 1;
            }

            while left <= right && nums.get(right as usize).unwrap().1 < pivot_freq {
                right -= 1;
            }

            if left > right {
                break;
            }

            Solution::swap(nums, left as usize, right as usize);

            left += 1;
            right -= 1;
        }

        if left as usize <= end {
            Solution::swap(nums, left as usize, end);
        }

        let pivot_idx = left;

        if k as i32 == pivot_idx + 1 {
            return nums[..k].iter().map(|(num, _)| *num).collect::<Vec<i32>>();
        }

        if (k as i32) < pivot_idx + 1 {
            return Solution::do_quick_select(nums, k, begin, pivot_idx as usize - 1);
        } else {
            return Solution::do_quick_select(nums, k, pivot_idx as usize + 1, end);
        }
    }

    pub fn quick_select(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut num_freq: HashMap<i32, i32> = HashMap::new();

        for num in nums {
            let freq = num_freq.entry(num).or_insert(0);
            *freq += 1;
        }

        let mut a: Vec<(i32, i32)> = num_freq.iter().map(|f| (*f.0, *f.1)).collect();

        Solution::do_quick_select(&mut a, k as usize, 0, num_freq.len() - 1)
    }

    pub fn bucket_sort(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut num_freq: HashMap<i32, i32> = HashMap::new();

        for num in nums.iter() {
            let freq = num_freq.entry(*num).or_insert(0);
            *freq += 1;
        }

        let mut freq_nums: HashMap<i32, Vec<i32>> = HashMap::new();

        for (num, freq) in num_freq {
            let nums = freq_nums.entry(freq).or_insert(vec![]);
            nums.push(num);
        }

        let mut count = 0;
        let mut freq = nums.len() as i32;
        let mut result = vec![];

        while count < k {
            match freq_nums.get_mut(&freq) {
                Some(arr) => {
                    count += arr.len() as i32;
                    result.append(arr);
                },
                None => {}
            }
            freq -= 1;
        }

        result
    }

    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        // Solution::priority_queue(nums, k)
        // Solution::quick_select(nums, k)
        Solution::bucket_sort(nums, k)
    }
}

fn main() {
    let nums = vec![1, 1, 1, 2, 2, 3];
    let k = 2;
    let res = Solution::top_k_frequent(nums, k);
    println!("res: {:#?}", res);
}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert!(Solution::compare_two_arrays(vec![1, 2], vec![2, 1]));

        let nums = vec![1, 1, 1, 2, 2, 3];
        let k = 2;
        let res = Solution::top_k_frequent(nums, k);
        println!("{:#?}", res);
        assert!(Solution::compare_two_arrays(res, vec![1, 2]));

        let nums = vec![1];
        let k = 1;
        assert!(Solution::compare_two_arrays(
            Solution::top_k_frequent(nums, k),
            vec![1]
        ));
    }

    #[test]
    fn test2() {
        let nums = vec![1, 2, 3];
        let k = 3;
        let res = Solution::top_k_frequent(nums, k);
        println!("{:#?}", res);
        assert!(Solution::compare_two_arrays(res, vec![1, 2, 3]));

        let nums = vec![1, 1, 2, 2];
        let k = 2;
        let res = Solution::top_k_frequent(nums, k);
        println!("{:#?}", res);
        assert!(Solution::compare_two_arrays(res, vec![1, 2]));
    }

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
