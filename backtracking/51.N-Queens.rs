use std::{collections::HashSet, vec};

struct Solution;

impl Solution {
    // because we have n queens and n rows, therefore each queen has to be placed in a different row.
    pub fn find_col_for_row(
        n: i32,       // table size
        row_idx: i32, // current row index
        selected_cols: &mut HashSet<i32>,
        selected_diagonal_down: &mut HashSet<i32>, // from top-left to bottom-right
        selected_diagonal_up: &mut HashSet<i32>,   // from bottom-left to top-right
        path: &mut Vec<(i32, i32)>,
    ) -> Vec<Vec<(i32, i32)>> {
        let path_len = path.len() as i32;
        if row_idx >= n && path_len == n {
            return vec![path.clone()];
        }

        let mut result: Vec<Vec<(i32, i32)>> = Vec::new();

        for col_idx in 0..n {
            let d_down = row_idx - col_idx;
            let d_up = row_idx + col_idx;
            if !selected_cols.contains(&col_idx)
                && !selected_diagonal_up.contains(&d_down)
                && !selected_diagonal_down.contains(&d_up)
            {
                selected_cols.insert(col_idx);
                selected_diagonal_up.insert(d_down);
                selected_diagonal_down.insert(d_up);
                path.push((row_idx, col_idx));

                let res = &mut Solution::find_col_for_row(
                    n,
                    row_idx + 1,
                    selected_cols,
                    selected_diagonal_down,
                    selected_diagonal_up,
                    path,
                );
                result.append(res);

                selected_cols.remove(&col_idx);
                selected_diagonal_up.remove(&d_down);
                selected_diagonal_down.remove(&d_up);
                path.pop();
            }
        }

        result
    }

    pub fn to_string(size: i32, paths: Vec<Vec<(i32, i32)>>) -> Vec<Vec<String>> {
        let mut result: Vec<Vec<String>> = Vec::new();

        for path in paths {
            let mut table_str: Vec<String> = Vec::new();
            for row in 0..size {
                let mut row_str = String::new();
                let (_, queen_col) = path.get(row as usize).unwrap();
                for col in 0..size {
                    if col == *queen_col {
                        row_str.push('Q');
                    } else {
                        row_str.push('.');
                    }
                }
                table_str.push(row_str);
            }
            result.push(table_str);
        }

        result
    }

    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let mut selected_cols: HashSet<i32> = HashSet::new();
        let mut selected_diagonal_down: HashSet<i32> = HashSet::new();
        let mut selected_diagonal_up: HashSet<i32> = HashSet::new();
        let mut path: Vec<(i32, i32)> = Vec::new();

        let paths = Solution::find_col_for_row(
            n,
            0,
            &mut selected_cols,
            &mut selected_diagonal_down,
            &mut selected_diagonal_up,
            &mut path,
        );

        Solution::to_string(n, paths)
    }
}
fn main() {}

#[cfg(test)]
mod tests {
    use crate::Solution;
    #[test]
    fn test_main() {
        let string = Solution::solve_n_queens(5);
        println!("{:#?}", string);
        let string = Solution::solve_n_queens(4);
        println!("{:#?}", string);
        let string = Solution::solve_n_queens(3);
        println!("{:#?}", string);
        let string = Solution::solve_n_queens(2);
        println!("{:#?}", string);
        let string = Solution::solve_n_queens(1);
        println!("{:#?}", string);
    }

    #[test]
    fn test_to_string() {
        let string = Solution::to_string(
            4,
            vec![
                vec![(0, 1), (1, 3), (2, 0), (3, 2)],
                vec![(0, 2), (1, 0), (2, 3), (3, 1)],
            ],
        );
        println!("{:#?}", string);
    }
}
