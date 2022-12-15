use std::{
    collections::{HashMap, HashSet},
    vec,
};

struct Solution;

impl Solution {
    pub fn build_adjacency(edges: &Vec<Vec<i32>>) -> HashMap<i32, HashSet<i32>> {
        let mut map: HashMap<i32, HashSet<i32>> = HashMap::new();

        for edge in edges {
            let vertice_1 = edge[0];
            let vertice_2 = edge[1];

            map.entry(vertice_1)
                .or_insert(HashSet::new())
                .insert(vertice_2);
            map.entry(vertice_2)
                .or_insert(HashSet::new())
                .insert(vertice_1);
        }

        map
    }

    pub fn dfs(
        map: &HashMap<i32, HashSet<i32>>,
        prev_edge: i32,
        curr_edge: i32,
        visited: &mut HashSet<i32>,
        path: &mut HashSet<i32>,
    ) -> bool {
        if visited.contains(&curr_edge) {
            return false;
        }
        if path.contains(&curr_edge) {
            // cyclic graph
            return true;
        }
        path.insert(curr_edge);
        for edge in map.get(&curr_edge).unwrap_or(&HashSet::new()) {
            if *edge != prev_edge {
                let cyclic_graph = Solution::dfs(map, curr_edge, *edge, visited, path);
                if cyclic_graph {
                    return true;
                }
            }
        }
        path.remove(&curr_edge);
        visited.insert(curr_edge);

        false
    }

    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let mut adjacency_list = Solution::build_adjacency(&edges);

        for edge_vec in edges.iter().rev() {
            let mut visited: HashSet<i32> = HashSet::new();

            let edge_1 = edge_vec[0];
            let edge_2 = edge_vec[1];

            adjacency_list.get_mut(&edge_1).unwrap().remove(&edge_2);
            adjacency_list.get_mut(&edge_2).unwrap().remove(&edge_1);

            let mut cyclic_graph = false;

            // println!("{:#?}", adjacency_list);

            for edge in 1..=edges.len() {
                cyclic_graph = Solution::dfs(
                    &adjacency_list,
                    0,
                    edge as i32,
                    &mut visited,
                    &mut HashSet::new(),
                );
                if cyclic_graph {
                    break;
                }
            }

            if !cyclic_graph {
                return edge_vec.clone();
            }

            adjacency_list.get_mut(&edge_1).unwrap().insert(edge_2);
            adjacency_list.get_mut(&edge_2).unwrap().insert(edge_1);
        }

        vec![0]
    }
}
fn main() {
    let res = Solution::find_redundant_connection(vec![
        vec![3, 5],
        vec![4, 5],
        vec![3, 4],
        vec![2, 3],
        vec![1, 2],
    ]);
    assert_eq!(res, vec![3, 4]);
}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        let res = Solution::find_redundant_connection(vec![vec![1, 2], vec![1, 3], vec![2, 3]]);
        assert_eq!(res, vec![2, 3]);
        let res = Solution::find_redundant_connection(vec![
            vec![1, 2],
            vec![2, 3],
            vec![3, 4],
            vec![1, 4],
            vec![1, 5],
        ]);
        assert_eq!(res, vec![1, 4]);
    }

    #[test]
    fn test3() {
        let res = Solution::find_redundant_connection(vec![
            vec![5, 0],
            vec![4, 0],
            vec![3, 0],
            vec![0, 1],
            vec![1, 2],
            vec![2, 3],
        ]);
        assert_eq!(res, vec![2, 3]);
    }

    #[test]
    fn test4() {
        let res = Solution::find_redundant_connection(vec![
            vec![2, 3],
            vec![2, 5],
            vec![4, 2],
            vec![1, 4],
            vec![1, 5],
        ]);
        assert_eq!(res, vec![1, 5]);
    }

    #[test]
    fn test2() {
        let res = Solution::find_redundant_connection(vec![
            vec![2, 7],
            vec![7, 8],
            vec![3, 6],
            vec![2, 5],
            vec![6, 8],
            vec![4, 8],
            vec![2, 8],
            vec![1, 8],
            vec![7, 10],
            vec![3, 9],
        ]);
        assert_eq!(res, vec![2, 8]);
    }

    #[test]
    fn test5() {
        let res = Solution::find_redundant_connection(vec![
            vec![3, 5],
            vec![4, 5],
            vec![3, 4],
            vec![2, 3],
            vec![1, 2],
        ]);
        assert_eq!(res, vec![3, 4]);
    }

    #[test]
    fn test_build_adjacency() {
        let res = Solution::build_adjacency(&vec![vec![1, 0]]);
        println!("{:#?}", res);
        let res = Solution::build_adjacency(&vec![vec![1, 0], vec![2, 0], vec![3, 1], vec![3, 2]]);
        println!("{:#?}", res);
        let res = Solution::build_adjacency(&vec![
            vec![5, 0],
            vec![4, 0],
            vec![0, 1],
            vec![1, 2],
            vec![2, 3],
        ]);
        println!("{:#?}", res);
    }
}
