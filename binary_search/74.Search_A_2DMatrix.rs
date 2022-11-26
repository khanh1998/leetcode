struct Solution;

impl Solution {
    // return index of row
    pub fn search_for_row(matrix: &Vec<Vec<i32>>, target: i32) -> Option<usize> {
        let row_count = matrix.len();
        let (mut left, mut right) = (0 as i32, (row_count - 1) as i32);

        loop {
            if left > right {
                break;
            }

            let mid_idx = (right + left) / 2;

            let mid_row = matrix.get(mid_idx as usize).unwrap();
            let (smallest, biggest) = (mid_row[0], mid_row.last().unwrap().to_owned());

            if target < smallest {
                right = mid_idx - 1;
            } else if target > biggest {
                left = mid_idx + 1;
            } else {
                return Some(mid_idx as usize);
            }
        }

        None
    }

    // return index of column
    pub fn search_for_column(row: &Vec<i32>, target: i32) -> Option<usize> {
        let length = row.len();
        let (mut left, mut right) = (0 as i32, (length - 1) as i32);

        loop {
            if left > right {
                break;
            }

            let mid = (right + left) / 2;
            let mid_val = row[mid as usize];

            if target < mid_val {
                right = mid - 1;
            } else if target > mid_val {
                left = mid + 1;
            } else {
                return Some(mid as usize);
            }
        }

        None
    }

    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        if let Some(row_idx) = Solution::search_for_row(&matrix, target) {
            if let Some(_) = Solution::search_for_column(&matrix[row_idx], target) {
                return true;
            }
        }

        false
    }
}

fn main() {}

#[cfg(test)]
mod test {
    use crate::Solution;

    #[test]
    fn search_matrix() {
        let matrix = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 60]];

        assert_eq!(Solution::search_matrix(matrix.clone(), 3), true);

        assert_eq!(Solution::search_matrix(matrix, 13), false,)
    }

    #[test]
    fn search_for_row() {
        let matrix = vec![vec![1]];
        assert_eq!(Solution::search_for_row(&matrix, 1), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 0), None);
        assert_eq!(Solution::search_for_row(&matrix, 2), None);
        let matrix = vec![vec![1, 3]];
        assert_eq!(Solution::search_for_row(&matrix, 1), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 3), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 2), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 0), None);
        assert_eq!(Solution::search_for_row(&matrix, 4), None);
        let matrix = vec![vec![1, 3, 5, 7]];
        assert_eq!(Solution::search_for_row(&matrix, 1), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 7), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 3), Some(0));

        assert_eq!(Solution::search_for_row(&matrix, 2), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 6), Some(0));

        assert_eq!(Solution::search_for_row(&matrix, 0), None);
        assert_eq!(Solution::search_for_row(&matrix, 9), None);
        let matrix = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20]];
        assert_eq!(Solution::search_for_row(&matrix, 1), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 7), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 3), Some(0));

        assert_eq!(Solution::search_for_row(&matrix, 2), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 6), Some(0));

        assert_eq!(Solution::search_for_row(&matrix, 0), None);
        assert_eq!(Solution::search_for_row(&matrix, 9), None);

        assert_eq!(Solution::search_for_row(&matrix, 10), Some(1));
        assert_eq!(Solution::search_for_row(&matrix, 20), Some(1));
        assert_eq!(Solution::search_for_row(&matrix, 16), Some(1));
        let matrix = vec![vec![1, 3, 5, 7], vec![10, 11, 16, 20], vec![23, 30, 34, 60]];
        assert_eq!(Solution::search_for_row(&matrix, 1), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 7), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 3), Some(0));

        assert_eq!(Solution::search_for_row(&matrix, 2), Some(0));
        assert_eq!(Solution::search_for_row(&matrix, 6), Some(0));

        assert_eq!(Solution::search_for_row(&matrix, 0), None);
        assert_eq!(Solution::search_for_row(&matrix, 9), None);

        assert_eq!(Solution::search_for_row(&matrix, 10), Some(1));
        assert_eq!(Solution::search_for_row(&matrix, 20), Some(1));
        assert_eq!(Solution::search_for_row(&matrix, 16), Some(1));
        assert_eq!(Solution::search_for_row(&matrix, 23), Some(2));
        assert_eq!(Solution::search_for_row(&matrix, 30), Some(2));
        assert_eq!(Solution::search_for_row(&matrix, 34), Some(2));
    }

    #[test]
    fn search_for_column() {
        assert_eq!(Solution::search_for_column(&vec![5], 5), Some(0));
        assert_eq!(Solution::search_for_column(&vec![1], 5), None);
        assert_eq!(Solution::search_for_column(&vec![1, 3], 3), Some(1));
        assert_eq!(Solution::search_for_column(&vec![1, 3], 1), Some(0));
        assert_eq!(Solution::search_for_column(&vec![1, 3], 5), None);
        assert_eq!(Solution::search_for_column(&vec![1, 3, 5], 5), Some(2));
        assert_eq!(Solution::search_for_column(&vec![1, 3, 5], 3), Some(1));
        assert_eq!(Solution::search_for_column(&vec![1, 3, 5], 1), Some(0));
        assert_eq!(Solution::search_for_column(&vec![1, 3, 5], 0), None);
        assert_eq!(Solution::search_for_column(&vec![1, 3, 5], 2), None);
        assert_eq!(Solution::search_for_column(&vec![1, 3, 5], 4), None);
        assert_eq!(Solution::search_for_column(&vec![1, 3, 5], 6), None);
    }
}
