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
    pub fn check(node_ref: &Option<Rc<RefCell<TreeNode>>>, max_so_far: i32) -> i32 {
        match node_ref {
            Some(node) => {
                let current_val = node.as_ref().borrow().val;

                let max_so_far = cmp::max(max_so_far, current_val);

                let left_count = Solution::check(&node.as_ref().borrow().left, max_so_far);
                let right_count = Solution::check(&node.as_ref().borrow().right, max_so_far);

                if current_val >= max_so_far {
                    return left_count + right_count + 1;
                }

                return left_count + right_count;
            }
            None => {
                return 0;
            }
        }
    }

    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Solution::check(&root, -10001)
    }
}
fn main() {}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn test1() {}
}
