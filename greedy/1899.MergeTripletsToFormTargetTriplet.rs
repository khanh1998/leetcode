use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn merge_triplets(triplets: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        let mut good = HashSet::new();

        for t in triplets {
            if t[0] > target[0] || t[1] > target[1] || t[2] > target[2] {
                continue;
            }

            for i in 0..3 {
                if t[i] == target[i] {
                    good.insert(i);
                }
            }
        }

        good.len() == 3
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(
            Solution::merge_triplets(
                vec![vec![2, 5, 3], vec![1, 8, 4], vec![1, 7, 5]],
                vec![2, 7, 5]
            ),
            true
        );
        assert_eq!(
            Solution::merge_triplets(vec![vec![3, 4, 5], vec![4, 5, 6]], vec![3, 2, 5]),
            false
        );
        assert_eq!(
            Solution::merge_triplets(
                vec![vec![2, 5, 3], vec![2, 3, 4], vec![1, 2, 5], vec![5, 2, 3]],
                vec![5, 5, 5]
            ),
            true
        );
    }

    #[test]
    fn test2() {}

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
