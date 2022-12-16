use std::collections::{HashMap};

struct Solution;

impl Solution {
    pub fn build_adjacency(edges: &Vec<Vec<String>>) -> HashMap<&String, Vec<(&String, usize)>> {
        let mut map: HashMap<&String, Vec<(&String, usize)>> = HashMap::new();

        for (index, edge) in edges.iter().enumerate() {
            let origin = &edge[0];
            let destination = &edge[1];

            map.entry(origin)
                .or_insert(Vec::new())
                .push((destination, index));
        }

        for (_, val) in map.iter_mut() {
            val.sort();
        }

        map
    }

    pub fn dfs<'a>(
        map: &HashMap<&'a String, Vec<(&'a String, usize)>>,
        path: &mut Vec<&'a String>,
        source: &'a String,
        remain_tickets: usize,
        used_tickets: &mut Vec<bool>,
    ) -> bool {
        if remain_tickets == 0 {
            return true;
        }

        if let Some(targets) = map.get(source) {
            for (target, ticket_idx) in targets {
                if used_tickets[*ticket_idx] == false {
                    path.push(&target);
                    used_tickets[*ticket_idx] = true;

                    let found = Solution::dfs(map, path, target, remain_tickets - 1, used_tickets);
                    if found {
                        return true;
                    }

                    path.pop();
                    used_tickets[*ticket_idx] = false;
                }
            }
        }

        false
    }

    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        let air_port = String::from("JFK");
        let map: HashMap<&String, Vec<(&String, usize)>> = Solution::build_adjacency(&tickets);
        let mut path: Vec<&String> = Vec::new();
        let mut used_tickets: Vec<bool> = vec![false; tickets.len()];
        path.push(&air_port);
        Solution::dfs(&map, &mut path, &air_port, tickets.len(), &mut used_tickets);
        path.iter().map(|x| (**x).clone()).collect()
    }
}
fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        let edges = vec![
            vec!["MUC".to_string(), "LHR".to_string()],
            vec!["JFK".to_string(), "MUC".to_string()],
            vec!["SFO".to_string(), "SJC".to_string()],
            vec!["LHR".to_string(), "SFO".to_string()],
        ];
        let res = Solution::find_itinerary(edges);
        let expected = vec![
            "JFK".to_string(),
            "MUC".to_string(),
            "LHR".to_string(),
            "SFO".to_string(),
            "SJC".to_string(),
        ];
        assert_eq!(res, expected);
    }

    #[test]
    fn test2() {
        let edges = vec![
            vec!["JFK".to_string(), "SFO".to_string()],
            vec!["JFK".to_string(), "ATL".to_string()],
            vec!["SFO".to_string(), "ATL".to_string()],
            vec!["ATL".to_string(), "JFK".to_string()],
            vec!["ATL".to_string(), "SFO".to_string()],
        ];
        let res = Solution::find_itinerary(edges);
        let expected = vec![
            "JFK".to_string(),
            "ATL".to_string(),
            "JFK".to_string(),
            "SFO".to_string(),
            "ATL".to_string(),
            "SFO".to_string(),
        ];
        assert_eq!(res, expected);
    }

    #[test]
    fn test3() {
        let edges = vec![
            vec!["JFK".to_string(), "KUL".to_string()],
            vec!["JFK".to_string(), "NRT".to_string()],
            vec!["NRT".to_string(), "JFK".to_string()],
        ];
        let res = Solution::find_itinerary(edges);
        let expected = vec![
            "JFK".to_string(),
            "NRT".to_string(),
            "JFK".to_string(),
            "KUL".to_string(),
        ];
        assert_eq!(res, expected);
    }

    #[test]
    fn test4() {
        let edges = vec![
            vec!["JFK".to_string(), "ATL".to_string()],
            vec!["ATL".to_string(), "JFK".to_string()],
        ];
        let res = Solution::find_itinerary(edges);
        let expected = vec!["JFK".to_string(), "ATL".to_string(), "JFK".to_string()];
        assert_eq!(res, expected);
    }

    #[test]
    fn test5() {
        let edges = vec![
            vec!["EZE".to_string(), "AXA".to_string()],
            vec!["TIA".to_string(), "ANU".to_string()],
            vec!["ANU".to_string(), "JFK".to_string()],
            vec!["JFK".to_string(), "ANU".to_string()],
            vec!["ANU".to_string(), "EZE".to_string()],
            vec!["TIA".to_string(), "ANU".to_string()],
            vec!["AXA".to_string(), "TIA".to_string()],
            vec!["TIA".to_string(), "JFK".to_string()],
            vec!["ANU".to_string(), "TIA".to_string()],
            vec!["JFK".to_string(), "TIA".to_string()],
        ];
        let res = Solution::find_itinerary(edges);
        let expected = vec![
            "JFK".to_string(),
            "ANU".to_string(),
            "EZE".to_string(),
            "AXA".to_string(),
            "TIA".to_string(),
            "ANU".to_string(),
            "JFK".to_string(),
            "TIA".to_string(),
            "ANU".to_string(),
            "TIA".to_string(),
            "JFK".to_string(),
        ];
        assert_eq!(res, expected);
    }

    #[test]
    fn test_build_adjacency() {
        let edges = vec![
            vec!["MUC".to_string(), "LHR".to_string()],
            vec!["JFK".to_string(), "MUC".to_string()],
            vec!["SFO".to_string(), "SJC".to_string()],
            vec!["LHR".to_string(), "SFO".to_string()],
        ];
        let res = Solution::build_adjacency(&edges);
        println!("{:#?}", res);

        let edges = vec![
            vec!["JFK".to_string(), "SFO".to_string()],
            vec!["JFK".to_string(), "ATL".to_string()],
            vec!["SFO".to_string(), "ATL".to_string()],
            vec!["ATL".to_string(), "JFK".to_string()],
            vec!["ATL".to_string(), "SFO".to_string()],
        ];
        let res = Solution::build_adjacency(&edges);
        println!("{:#?}", res);

        let edges = vec![
            vec!["EZE".to_string(), "AXA".to_string()],
            vec!["TIA".to_string(), "ANU".to_string()],
            vec!["ANU".to_string(), "JFK".to_string()],
            vec!["JFK".to_string(), "ANU".to_string()],
            vec!["ANU".to_string(), "EZE".to_string()],
            vec!["TIA".to_string(), "ANU".to_string()],
            vec!["AXA".to_string(), "TIA".to_string()],
            vec!["TIA".to_string(), "JFK".to_string()],
            vec!["ANU".to_string(), "TIA".to_string()],
            vec!["JFK".to_string(), "TIA".to_string()],
        ];
        let res = Solution::build_adjacency(&edges);
        println!("{:#?}", res);
    }
}
