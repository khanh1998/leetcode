use std::cmp;

struct MinStack {
    data: Vec<(i32, i32)>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {
    fn new() -> Self {
        MinStack { data: Vec::new() }
    }

    fn push(&mut self, val: i32) {
        if self.data.len() == 0 {
            self.data.push((val, val))
        } else {
            let min = cmp::min(self.get_min(), val);
            self.data.push((min, val))
        }
    }

    fn pop(&mut self) {
        match self.data.pop() {
            Some(_) => {}
            None => {}
        }
    }

    fn top(&self) -> i32 {
        match self.data.last() {
            Some(item) => {
                let (_min_so_far, number) = item;
                *number
            }
            None => 0,
        }
    }

    fn get_min(&self) -> i32 {
        match self.data.last() {
            Some(item) => {
                let (min_so_far, _number) = item;
                *min_so_far
            }
            None => 0,
        }
    }
}

fn main() {
    let mut obj = MinStack::new();
    obj.push(-2);
    obj.push(0);
    obj.push(-3);
    assert_eq!(-3, obj.get_min());
    obj.pop();
    assert_eq!(0, obj.top());
    assert_eq!(-2, obj.get_min());
    // test 2
    let mut obj = MinStack::new();
    obj.push(5);
    assert_eq!(5, obj.get_min());
    assert_eq!(5, obj.top());
    obj.push(4);
    assert_eq!(4, obj.get_min());
    assert_eq!(4, obj.top());
    obj.push(6);
    assert_eq!(4, obj.get_min());
    assert_eq!(6, obj.top());
    obj.pop();
    obj.push(3);
    assert_eq!(3, obj.get_min());
    assert_eq!(3, obj.top());
    // test 3
    let mut obj = MinStack::new();
    obj.push(1);
    assert_eq!(1, obj.get_min());
    assert_eq!(1, obj.top());
    obj.pop();
    assert_eq!(0, obj.data.len());
}
