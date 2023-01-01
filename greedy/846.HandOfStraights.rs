struct Solution;

impl Solution {
    pub fn is_n_straight_hand(mut hand: Vec<i32>, group_size: i32) -> bool {
        hand.sort();
        let length = hand.len();
        let mut selected = vec![false; length];
        let mut selected_count = 0;
        let mut start = 0;

        loop {
            if selected_count == length {
                return true;
            }

            // find new start position from previous start.
            for i in start..length {
                if selected[i] == false {
                    start = i;
                    break;
                }
            }

            // find other next consecutive values.
            selected[start] = true;
            selected_count += 1;
            let mut next_val = hand[start] + 1;
            let mut count = 1;

            for i in start + 1..length {
                if hand[i] == next_val && count < group_size && !selected[i] {
                    count += 1;
                    selected[i] = true;
                    selected_count += 1;
                    next_val += 1;
                }

                if count == group_size {
                    break;
                }
            }

            if count != group_size {
                return false;
            }
        }

        true
    }
}

fn main() {
    Solution::is_n_straight_hand(vec![1, 2, 3, 6, 2, 3, 4, 7, 8], 3);
}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(
            Solution::is_n_straight_hand(vec![1, 2, 3, 6, 2, 3, 4, 7, 8], 3),
            true
        );
        assert_eq!(Solution::is_n_straight_hand(vec![1, 2, 3, 4, 5], 4), false)
    }

    #[test]
    fn test2() {
        assert_eq!(Solution::is_n_straight_hand(vec![2], 1), true);
        assert_eq!(Solution::is_n_straight_hand(vec![2, 3], 1), true);
        assert_eq!(Solution::is_n_straight_hand(vec![3, 3, 3], 1), true);
        assert_eq!(Solution::is_n_straight_hand(vec![1, 1, 2, 2], 2), true);
        assert_eq!(Solution::is_n_straight_hand(vec![2, 2, 2], 3), false);
        assert_eq!(
            Solution::is_n_straight_hand(vec![2, 2, 2, 1, 1, 1], 3),
            false
        );
    }

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
