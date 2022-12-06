use std::{collections::HashSet};

struct Solution;

impl Solution {
    fn calc(nums: &Vec<i32>, picked_nums: &mut HashSet<i32>, path: &mut Vec<i32>) -> Vec<Vec<i32>> {
        if nums.len() == picked_nums.len() {
            return vec![path.to_vec()];
        }

        let mut result: Vec<Vec<i32>> = vec![];
        for num in nums {
            if !picked_nums.contains(num) {
                picked_nums.insert(*num);
                path.push(*num);

                let answer = &mut Solution::calc(nums, picked_nums, path);
                result.append(answer);

                picked_nums.remove(num);
                path.pop();
            }
        }

        result
    }

    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let candidate: &mut HashSet<i32> = &mut HashSet::new();
        let mut path: &mut Vec<i32> = &mut Vec::new();

        return Solution::calc(&nums, candidate, path);
    }
}
