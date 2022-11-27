use std::collections::HashMap;

struct TimeMap {
    data: HashMap<String, Vec<(i32, String)>>,
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            data: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.data
            .entry(key)
            .or_insert(vec![(timestamp, value.to_owned())])
            .push((timestamp, value));
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        if let Some(arr) = self.data.get(&key) {
            let (mut left, mut right) = (0 as i32, (arr.len() - 1) as i32);
            let mut result = String::from("");

            loop {
                if left > right {
                    break;
                }

                let mid_idx = (left + right) / 2;
                let (time, value) = &arr[mid_idx as usize];

                if *time > timestamp {
                    right = mid_idx - 1;
                } else if *time < timestamp {
                    result = value.clone();
                    left = mid_idx + 1;
                } else {
                    result = value.clone();
                    break;
                }
            }

            return result;
        }
        String::from("")
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use crate::TimeMap;

    #[test]
    fn test1() {
        let mut obj = TimeMap::new();
        obj.set(String::from("foo"), String::from("bar"), 1);
        assert_eq!(obj.get(String::from("foo"), 1), String::from("bar"));
        assert_eq!(obj.get(String::from("foo"), 3), String::from("bar"));
        obj.set(String::from("foo"), String::from("bar2"), 4);
        assert_eq!(obj.get(String::from("foo"), 4), String::from("bar2"));
        assert_eq!(obj.get(String::from("foo"), 5), String::from("bar2"));
    }

    #[test]
    fn test2() {
        let mut obj = TimeMap::new();
        assert_eq!(obj.get(String::from("foo"), 1), String::from(""));
    }

    #[test]
    fn test3() {
        let mut obj = TimeMap::new();
        obj.set(String::from("foo"), String::from("bar"), 2);
        obj.set(String::from("foo1"), String::from("bar1"), 3);
        assert_eq!(obj.get(String::from("foo1"), 1), String::from(""));
        assert_eq!(obj.get(String::from("foo1"), 3), String::from("bar1"));
        assert_eq!(obj.get(String::from("foo1"), 4), String::from("bar1"));
        assert_eq!(obj.get(String::from("foo"), 1), String::from(""));
        assert_eq!(obj.get(String::from("foo"), 2), String::from("bar"));
        assert_eq!(obj.get(String::from("foo"), 3), String::from("bar"));
    }

    #[test]
    fn test4() {
        let mut obj = TimeMap::new();
        obj.set(String::from("foo"), String::from("bar"), 2);
        obj.set(String::from("foo"), String::from("bar1"), 4);
        obj.set(String::from("foo"), String::from("bar2"), 6);
        obj.set(String::from("foo"), String::from("bar3"), 8);
        obj.set(String::from("foo"), String::from("bar4"), 10);
        assert_eq!(obj.get(String::from("foo"), 1), String::from(""));
        assert_eq!(obj.get(String::from("foo"), 2), String::from("bar"));
        assert_eq!(obj.get(String::from("foo"), 3), String::from("bar"));
        assert_eq!(obj.get(String::from("foo"), 4), String::from("bar1"));
        assert_eq!(obj.get(String::from("foo"), 5), String::from("bar1"));
        assert_eq!(obj.get(String::from("foo"), 6), String::from("bar2"));
        assert_eq!(obj.get(String::from("foo"), 7), String::from("bar2"));
        assert_eq!(obj.get(String::from("foo"), 8), String::from("bar3"));
        assert_eq!(obj.get(String::from("foo"), 9), String::from("bar3"));
        assert_eq!(obj.get(String::from("foo"), 10), String::from("bar4"));
        assert_eq!(obj.get(String::from("foo"), 11), String::from("bar4"));
    }
}
