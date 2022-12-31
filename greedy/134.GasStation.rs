struct Solution;

impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let length = gas.len();

        let total_gas: i32 = gas.iter().sum();
        let total_cost: i32 = cost.iter().sum();

        if total_gas < total_cost {
            return -1;
        }

        let mut tank = 0;
        let mut result: i32 = 0;

        for start in 0..length {
            tank += gas[start] - cost[start];
            if tank < 0 {
                result = (start + 1) as i32;
                tank = 0;
            }
        }

        result
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
            Solution::can_complete_circuit(vec![1, 2, 3, 4, 5], vec![3, 4, 5, 1, 2]),
            3,
        );

        assert_eq!(
            Solution::can_complete_circuit(vec![2, 3, 4], vec![3, 4, 3]),
            -1,
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
