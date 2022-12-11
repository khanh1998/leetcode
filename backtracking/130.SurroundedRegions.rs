use std::vec;

struct Solution;

impl Solution {
    pub fn is_point_valid(board: &mut Vec<Vec<char>>, row: i32, col: i32) -> bool {
        let rows = board.len() as i32;
        let cols = board.first().unwrap().len() as i32;
        if row >= 0 && col >= 0 && row < rows && col < cols {
            return true;
        }

        false
    }

    pub fn is_on_edge(board: &mut Vec<Vec<char>>, row: i32, col: i32) -> bool {
        let rows = board.len() as i32;
        let cols = board.first().unwrap().len() as i32;

        return row == 0 || col == 0 || row == rows - 1 || col == cols - 1;
    }

    pub fn calc(
        board: &mut Vec<Vec<char>>,
        visited: &mut Vec<Vec<bool>>,
        row: i32,
        col: i32,
        path: &mut Vec<(i32, i32)>,
        prev_on_edge: &mut bool,
    ) {
        let directions = vec![(-1, 0), (0, 1), (1, 0), (0, -1)];

        if Solution::is_point_valid(board, row, col) {
            let visit = &mut visited[row as usize][col as usize];
            let cell = board[row as usize][col as usize];

            if *visit == false {
                *visit = true;
            } else {
                return;
            }

            if cell == 'O' {
                if Solution::is_on_edge(board, row, col) {
                    *prev_on_edge = true;
                }

                path.push((row, col));

                for (d_row, d_col) in directions {
                    Solution::calc(board, visited, row + d_row, col + d_col, path, prev_on_edge);
                }
            } else {
                return;
            }
        } else {
            return;
        }
    }

    pub fn solve(board: &mut Vec<Vec<char>>) {
        let rows = board.len();
        let cols = board.first().unwrap().len();
        let visited = &mut vec![vec![false; cols]; rows];
        for row in 0..rows {
            for col in 0..cols {
                let is_on_edge = &mut Solution::is_on_edge(board, row as i32, col as i32);
                let path: &mut Vec<(i32, i32)> = &mut vec![];

                Solution::calc(board, visited, row as i32, col as i32, path, is_on_edge);
                if *is_on_edge == false {
                    for (i_row, i_col) in path {
                        board[*i_row as usize][*i_col as usize] = 'X';
                    }
                }
            }
        }
    }
}
fn main() {}

#[cfg(test)]
mod tests {
    use crate::Solution;
    fn print_vec(board: &Vec<Vec<char>>) {
        for row in board {
            for val in row {
                print!("{val}, ")
            }
            println!();
        }
        println!();
    }

    #[test]
    fn test5() {
        let mut board = vec![
            vec!['X', 'O', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'O'],
            vec!['X', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'X'],
            vec!['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
            vec!['O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X'],
            vec!['O', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'O', 'O'],
            vec!['X', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'O'],
            vec!['X', 'O', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O'],
            vec!['X', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'O', 'X'],
            vec!['O', 'O', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'O'],
            vec!['X', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'O'],
        ];

        let expected = vec![
            vec!['X', 'O', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'O'],
            vec!['X', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'X'],
            vec!['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
            vec!['O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'X'],
            vec!['O', 'O', 'X', 'X', 'O', 'X', 'X', 'O', 'O', 'O'],
            vec!['X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O'],
            vec!['X', 'O', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'O'],
            vec!['X', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'X'],
            vec!['O', 'O', 'O', 'O', 'X', 'X', 'X', 'O', 'X', 'O'],
            vec!['X', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'O'],
        ];

        Solution::solve(&mut board);
        print_vec(&board);
        assert_eq!(board, expected);
    }

    #[test]
    fn test1() {
        let mut board = vec![
            vec!['X', 'X', 'X', 'X'],
            vec!['X', 'O', 'O', 'X'],
            vec!['X', 'X', 'O', 'X'],
            vec!['X', 'O', 'X', 'X'],
        ];
        Solution::solve(&mut board);
        print_vec(&board);
        let mut board = vec![vec!['X']];
        Solution::solve(&mut board);
        print_vec(&board);
        let mut board = vec![vec!['O']];
        Solution::solve(&mut board);
        print_vec(&board);
    }

    #[test]
    fn test4() {
        let mut board = vec![
            vec!['O', 'X', 'O', 'O', 'O', 'X'],
            vec!['O', 'O', 'X', 'X', 'X', 'O'],
            vec!['X', 'X', 'X', 'X', 'X', 'O'],
            vec!['O', 'O', 'O', 'O', 'X', 'X'],
            vec!['X', 'X', 'O', 'O', 'X', 'O'],
            vec!['O', 'O', 'X', 'X', 'X', 'X'],
        ];
        Solution::solve(&mut board);
        print_vec(&board);
    }

    #[test]
    fn test3() {
        let mut board = vec![
            vec!['X', 'X', 'X'],
            vec!['X', 'O', 'X'],
            vec!['X', 'X', 'X'],
        ];
        Solution::solve(&mut board);
        print_vec(&board);

        let mut board = vec![
            vec!['X', 'X', 'X'],
            vec!['X', 'O', 'O'],
            vec!['X', 'X', 'X'],
        ];
        Solution::solve(&mut board);
        print_vec(&board);

        let mut board = vec![
            vec!['X', 'X', 'X'],
            vec!['O', 'O', 'X'],
            vec!['X', 'X', 'X'],
        ];
        Solution::solve(&mut board);
        print_vec(&board);

        let mut board = vec![
            vec!['X', 'O', 'X'],
            vec!['X', 'O', 'X'],
            vec!['X', 'X', 'X'],
        ];
        Solution::solve(&mut board);
        print_vec(&board);
    }

    #[test]
    fn test2() {
        let mut board = vec![vec!['X', 'X'], vec!['X', 'X']];
        Solution::solve(&mut board);
        print_vec(&board);
        let mut board = vec![vec!['O', 'X'], vec!['X', 'X']];
        Solution::solve(&mut board);
        print_vec(&board);
        let mut board = vec![vec!['X', 'O'], vec!['X', 'X']];
        Solution::solve(&mut board);
        print_vec(&board);
        let mut board = vec![vec!['X', 'X'], vec!['O', 'X']];
        Solution::solve(&mut board);
        print_vec(&board);
        let mut board = vec![vec!['X', 'X'], vec!['X', 'O']];
        Solution::solve(&mut board);
        print_vec(&board);
        let mut board = vec![vec!['O', 'O'], vec!['X', 'X']];
        Solution::solve(&mut board);
        print_vec(&board);
        let mut board = vec![vec!['X', 'X'], vec!['O', 'O']];
        Solution::solve(&mut board);
        print_vec(&board);
    }
}
