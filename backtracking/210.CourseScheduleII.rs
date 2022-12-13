use std::{
    collections::{HashMap, HashSet},
    vec,
};

struct Solution;

impl Solution {
    pub fn build_adjacency(prerequisites: Vec<Vec<i32>>) -> HashMap<i32, Vec<i32>> {
        let mut map: HashMap<i32, Vec<i32>> = HashMap::new();

        for prerequisite in prerequisites {
            let course = prerequisite[0];
            let prereq = prerequisite[1];

            map.entry(course).or_insert(vec![]).push(prereq);
        }

        map
    }

    pub fn topo(
        course: i32,
        prerequisites: &HashMap<i32, Vec<i32>>,
        answer: &mut Vec<i32>,
        visited: &mut HashSet<i32>,
        path: &mut HashSet<i32>,
    ) -> bool {
        if visited.contains(&course) {
            return false;
        }

        if path.contains(&course) {
            return true; // cyclic graph
        }

        path.insert(course);

        for prere in prerequisites.get(&course).unwrap_or(&vec![]) {
            let cyclic_graph = Solution::topo(*prere, prerequisites, answer, visited, path);
            if cyclic_graph {
                return true;
            }
        }

        path.remove(&course);

        visited.insert(course);

        answer.push(course);

        return false;
    }

    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let mut answer: Vec<i32> = Vec::new();
        let mut visited: HashSet<i32> = HashSet::new();
        let map = Solution::build_adjacency(prerequisites);

        for course in 0..num_courses {
            let cyclic_graph =
                Solution::topo(course, &map, &mut answer, &mut visited, &mut HashSet::new());

            if cyclic_graph {
                return vec![];
            }
        }

        answer.into_iter().collect()
    }
}
fn main() {
    let res = Solution::find_order(
        6,
        vec![vec![5, 0], vec![4, 0], vec![0, 1], vec![1, 2], vec![2, 3]],
    );
    let expected = vec![3, 2, 1, 0, 4, 5];
    assert_eq!(res, expected);
}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        let res = Solution::find_order(2, vec![vec![1, 0]]);
        let expected = vec![0, 1];
        assert_eq!(res, expected);

        let res = Solution::find_order(1, vec![]);
        let expected = vec![0];
        assert_eq!(res, expected);

        let res = Solution::find_order(4, vec![vec![1, 0], vec![2, 0], vec![3, 1], vec![3, 2]]);
        let expected = vec![0, 1, 2, 3];
        assert_eq!(res, expected);
    }

    #[test]
    fn test3() {
        let res = Solution::find_order(
            6,
            vec![vec![5, 0], vec![4, 0], vec![0, 1], vec![1, 2], vec![2, 3]],
        );
        let expected = vec![3, 2, 1, 0, 4, 5];
        assert_eq!(res, expected);

        let res = Solution::find_order(6, vec![]);
        let expected = vec![0, 1, 2, 3, 4, 5];
        assert_eq!(res, expected);
    }

    #[test]
    fn test2() {
        // cyclic graph
        let res = Solution::find_order(2, vec![vec![1, 0], vec![0, 1]]);
        let expected = vec![];
        assert_eq!(res, expected);

        let res = Solution::find_order(3, vec![vec![1, 0], vec![0, 1]]);
        let expected = vec![];
        assert_eq!(res, expected);

        let res = Solution::find_order(3, vec![vec![1, 0], vec![2, 1], vec![0, 2]]);
        let expected = vec![];
        assert_eq!(res, expected);
    }

    #[test]
    fn test_build_adjacency() {
        let res = Solution::build_adjacency(vec![vec![1, 0]]);
        println!("{:#?}", res);
        let res = Solution::build_adjacency(vec![vec![1, 0], vec![2, 0], vec![3, 1], vec![3, 2]]);
        println!("{:#?}", res);
        let res = Solution::build_adjacency(vec![
            vec![5, 0],
            vec![4, 0],
            vec![0, 1],
            vec![1, 2],
            vec![2, 3],
        ]);
        println!("{:#?}", res);
    }
}
