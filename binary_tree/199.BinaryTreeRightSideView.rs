// Definition for a binary tree node.
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

struct Solution;

use std::cell::RefCell;
use std::rc::Rc;
use std::vec;

impl Solution {
    pub fn find(
        node: &Option<Rc<RefCell<TreeNode>>>,
        height: usize,
        mut values: Vec<i32>,
    ) -> Vec<i32> {
        match &node {
            Some(val) => {
                if values.len() < height {
                    values.push(val.borrow().val);
                }

                let right = Solution::find(&val.borrow().right, height + 1, values);

                let left = Solution::find(&val.borrow().left, height + 1, right);

                return left;
            }
            None => values,
        }
    }

    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        Solution::find(&root, 1, vec![])
    }
}
fn main() {}

#[cfg(test)]
mod tests {
    use crate::Solution;


    #[test]
    fn test1() {
    }
}
