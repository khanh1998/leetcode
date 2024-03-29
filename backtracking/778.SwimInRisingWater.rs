use std::{
    cmp::{max, Reverse},
    collections::{BinaryHeap, HashSet},
};

struct Solution;

impl Solution {
    fn valid(
        next_row: i32,
        next_col: i32,
        target: (i32, i32),
        visited: &HashSet<(i32, i32)>,
    ) -> bool {
        if next_row < 0
            || next_col < 0
            || next_row > target.0
            || next_col > target.1
            || visited.contains(&(next_row, next_col))
        {
            return false;
        }

        true
    }
    pub fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
        let mut visited: HashSet<(i32, i32)> = HashSet::new();
        let mut candidate: BinaryHeap<Reverse<(&i32, i32, i32)>> = BinaryHeap::new();
        let N = grid.len() as i32;
        let target = (N - 1, N - 1);
        let directions = vec![(-1, 0), (0, 1), (1, 0), (0, -1)];

        candidate.push(Reverse((&grid[0][0], 0, 0)));
        visited.insert((0, 0));

        loop {
            let next_candidate = candidate.pop();

            if let Some(Reverse((val, row, col))) = next_candidate {
                if (row, col) == target {
                    return *val;
                }

                for (r, c) in directions.iter() {
                    let next_row = row + r;
                    let next_col = col + c;
                    if Solution::valid(next_row, next_col, target, &visited) {
                        visited.insert((next_row, next_col));
                        let next_val = &grid[next_row as usize][next_col as usize];
                        candidate.push(Reverse((max(next_val, val), next_row, next_col)));
                    }
                }
            } else {
                break;
            }
        }

        -1
    }
}
fn main() {
    let res = Solution::swim_in_water(vec![vec![0, 1, 2], vec![1, 2, 3], vec![2, 3, 4]]);
    assert_eq!(res, 4);
}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        let res = Solution::swim_in_water(vec![vec![3]]);
        assert_eq!(res, 3);
        let res = Solution::swim_in_water(vec![vec![0, 2], vec![1, 3]]);
        assert_eq!(res, 3);
        let res = Solution::swim_in_water(vec![vec![0, 1, 3], vec![2, 4, 1], vec![1, 2, 1]]);
        assert_eq!(res, 2);
        let res = Solution::swim_in_water(vec![
            vec![0, 1, 2, 3, 4],
            vec![24, 23, 22, 21, 5],
            vec![12, 13, 14, 15, 16],
            vec![11, 17, 18, 19, 20],
            vec![10, 9, 8, 7, 6],
        ]);
        assert_eq!(res, 16);
    }

    #[test]
    fn test2() {
        let input = vec![
            vec![
                375, 396, 190, 333, 304, 65, 99, 262, 214, 344, 167, 328, 124, 207, 253, 173, 55,
                243, 132, 163,
            ],
            vec![
                22, 12, 223, 298, 387, 238, 237, 213, 332, 379, 228, 128, 280, 225, 103, 114, 109,
                64, 271, 172,
            ],
            vec![
                359, 26, 80, 18, 370, 372, 206, 346, 342, 363, 184, 11, 393, 317, 291, 362, 194,
                308, 274, 188,
            ],
            vec![
                288, 158, 153, 260, 278, 296, 40, 231, 397, 334, 4, 7, 181, 219, 189, 101, 54, 112,
                292, 25,
            ],
            vec![
                391, 195, 165, 268, 248, 388, 143, 266, 87, 250, 204, 358, 187, 275, 32, 127, 66,
                115, 146, 234,
            ],
            vec![
                313, 218, 8, 19, 50, 164, 279, 23, 182, 73, 392, 74, 149, 323, 107, 283, 203, 302,
                148, 28,
            ],
            vec![
                326, 162, 301, 41, 131, 306, 96, 200, 160, 44, 137, 300, 398, 170, 94, 309, 38, 16,
                83, 129,
            ],
            vec![
                245, 339, 72, 310, 117, 140, 264, 366, 252, 314, 361, 282, 230, 353, 325, 374, 180,
                351, 68, 77,
            ],
            vec![
                205, 340, 367, 169, 209, 255, 221, 152, 226, 354, 381, 319, 285, 136, 138, 175,
                389, 273, 35, 142,
            ],
            vec![
                286, 249, 395, 81, 390, 37, 303, 338, 220, 71, 242, 399, 82, 176, 168, 263, 299,
                51, 1, 125,
            ],
            vec![
                198, 355, 133, 15, 210, 151, 376, 294, 3, 235, 336, 76, 113, 281, 122, 110, 257,
                343, 246, 159,
            ],
            vec![
                394, 92, 384, 316, 123, 211, 324, 329, 5, 284, 212, 239, 48, 224, 196, 9, 236, 119,
                147, 233,
            ],
            vec![
                20, 24, 331, 183, 90, 45, 106, 201, 70, 276, 186, 320, 13, 256, 202, 91, 352, 69,
                178, 116,
            ],
            vec![
                105, 10, 121, 86, 111, 385, 98, 139, 141, 269, 100, 95, 327, 130, 287, 58, 382,
                126, 297, 191,
            ],
            vec![
                272, 364, 222, 330, 53, 232, 118, 97, 63, 365, 322, 36, 185, 270, 47, 277, 241, 49,
                373, 369,
            ],
            vec![
                75, 0, 57, 193, 199, 357, 43, 60, 145, 360, 267, 134, 120, 29, 337, 349, 161, 62,
                254, 350,
            ],
            vec![
                348, 240, 78, 311, 371, 318, 17, 259, 335, 251, 31, 88, 341, 14, 39, 85, 217, 108,
                293, 144,
            ],
            vec![
                290, 46, 56, 104, 156, 356, 229, 377, 177, 347, 261, 52, 179, 345, 289, 135, 59,
                34, 265, 295,
            ],
            vec![
                386, 380, 27, 2, 6, 307, 192, 378, 33, 89, 84, 30, 102, 321, 197, 157, 61, 368, 67,
                383,
            ],
            vec![
                154, 312, 155, 215, 21, 315, 216, 150, 93, 79, 305, 174, 42, 227, 208, 244, 247,
                258, 166, 171,
            ],
        ];
        let res = Solution::swim_in_water(input);
        assert_eq!(res, 375);
    }

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
