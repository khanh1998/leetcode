struct Solution;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;
impl Solution {
    pub fn zigzag_level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        if let None = root {
            return vec![]
        }

        let mut queue: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        queue.push_back(root.unwrap());

        let mut right_to_left = false;

        while !queue.is_empty() {
            let length = queue.len();
            let mut level: Vec<i32> = vec![];
            for _ in 0..length {
                let item = queue.pop_front().unwrap();
                if right_to_left {
                    level.insert(0, item.borrow().val);
                } else {
                    level.push(item.borrow().val);
                }
                if let Some(left) = item.borrow().left.clone() {
                    queue.push_back(Rc::clone(&left));
                };
                if let Some(right) = item.borrow().right.clone() {
                    queue.push_back(Rc::clone(&right));
                };
            }

            result.push(level);
            right_to_left = !right_to_left
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
    fn test1() {}

    #[test]
    fn test2() {}

    #[test]
    fn test3() {}

    #[test]
    fn test4() {}

    #[test]
    fn test5() {}
}
