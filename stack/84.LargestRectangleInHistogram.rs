struct Solution;

use std::cmp;

#[derive(Debug)]
struct Item {
    left_boundary: usize,
    height: i32,
}

impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let length = heights.len();
        if length == 1 {
            return heights[0];
        }

        let mut max_area: i32 = 0;
        let mut stack: Vec<Item> = Vec::new();
        stack.push(Item {
            left_boundary: 0,
            height: heights[0],
        });

        for i in 1..length {
            let curr_height = heights[i];
            let mut left_boundary: Option<usize> = None;

            // println!("step {i} height {curr_height} stack: {:#?}", stack);

            loop {
                let mut do_pop = false;
                if let Some(top) = stack.last() {
                    if top.height > curr_height {
                        do_pop = true;
                    }
                }

                if do_pop {
                    let top = stack.pop().unwrap();
                    let width = (i - top.left_boundary) as i32;
                    let area: i32 = width * top.height;

                    max_area = cmp::max(max_area, area);

                    left_boundary = Some(top.left_boundary);
                } else {
                    let left_boundary = left_boundary.unwrap_or(i);
                    
                    stack.push(Item {
                        left_boundary,
                        height: curr_height,
                    });

                    break;
                }
            }

            // println!("step {i} max {max_area}")
        }
        // println!("{:#?}", stack);

        loop {
            match stack.pop() {
                Some(top) => {
                    let width = (length - top.left_boundary) as i32;
                    let area = width * top.height;
                    max_area = cmp::max(max_area, area);
                }
                None => break,
            }
        }

        max_area
    }
}

fn main() {
    assert_eq!(
        Solution::largest_rectangle_area(vec![2, 1, 4, 3, 6, 5, 8, 7, 10, 9]),
        30
    );
    assert_eq!(
        Solution::largest_rectangle_area(vec![2, 1, 4, 3, 6, 5, 8, 7, 10, 9]),
        30
    );
    assert_eq!(
        Solution::largest_rectangle_area(vec![5, 4, 3, 2, 3, 4, 5]),
        14
    );
    assert_eq!(Solution::largest_rectangle_area(vec![2, 1, 5, 6, 2, 3]), 10);
    assert_eq!(Solution::largest_rectangle_area(vec![0, 4]), 4);
    assert_eq!(Solution::largest_rectangle_area(vec![1, 4]), 4);
    assert_eq!(Solution::largest_rectangle_area(vec![2, 4]), 4);
    assert_eq!(Solution::largest_rectangle_area(vec![3, 4]), 6);
    assert_eq!(Solution::largest_rectangle_area(vec![4, 3]), 6);
    assert_eq!(Solution::largest_rectangle_area(vec![4, 2]), 4);
    assert_eq!(Solution::largest_rectangle_area(vec![4, 1]), 4);
    assert_eq!(Solution::largest_rectangle_area(vec![4, 0]), 4);
    assert_eq!(Solution::largest_rectangle_area(vec![1, 2, 3]), 4);
    assert_eq!(Solution::largest_rectangle_area(vec![3, 2, 1]), 4);
    assert_eq!(Solution::largest_rectangle_area(vec![2, 3, 1]), 4);
    assert_eq!(Solution::largest_rectangle_area(vec![2, 1, 3]), 3);
    assert_eq!(
        Solution::largest_rectangle_area(vec![1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9]),
        21
    );
    assert_eq!(Solution::largest_rectangle_area(vec![0]), 0);
    assert_eq!(Solution::largest_rectangle_area(vec![1]), 1);
}
