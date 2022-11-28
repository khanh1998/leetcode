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
use std::cmp;
use std::rc::Rc;

impl Solution {
    pub fn get_height(node: &Option<Rc<RefCell<TreeNode>>>) -> (u32, bool) {
        match node {
            Some(val) => {
                let (left_height, left_balance) = Solution::get_height(&val.borrow().left);
                let (right_height, right_balance) = Solution::get_height(&val.borrow().right);

                let height = cmp::max(left_height, right_height) + 1;
                let height_diff = (left_height as i32 - right_height as i32).abs();

                if left_balance && right_balance && height_diff <= 1 {
                    return (height, true);
                }

                return (height, false);
            }
            None => {
                return (0, true);
            }
        }
    }

    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let (_, balance) = Solution::get_height(&root);

        balance
    }
}
fn main() {}

#[cfg(test)]
mod tests {

    #[test]
    fn test1() {}
}
