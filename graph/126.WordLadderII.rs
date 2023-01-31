struct Solution;

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    fn is_differ_by_a_letter(word1: &str, word2: &str) -> bool {
        let mut diff_count = 0;
        let length1 = word1.len();
        let length2 = word2.len();
        if length1 != length2 {
            return false;
        }
        for i in 0..length1 {
            if word1.chars().nth(i).unwrap() != word2.chars().nth(i).unwrap() {
                diff_count += 1;
            }
        }
        return diff_count == 1;
    }

    fn build_adjacency_list<'a>(
        word_list: &'a Vec<String>,
        begin_word: &'a str,
    ) -> HashMap<&'a str, HashSet<&'a str>> {
        let mut result = HashMap::new();
        let mut word_set: HashSet<&str> = HashSet::new();
        word_set.insert(begin_word);
        for word in word_list {
            word_set.insert(word.as_ref());
        }

        let mut input: Vec<&str> = word_list.iter().map(|s| s.as_ref()).collect();
        input.push(begin_word);

        for word in input {
            for i in 0..word.len() {
                for c in b'a'..=b'z' {
                    // a -> z
                    let mut next = word.to_string();
                    next.remove(i);
                    next.insert(i, c as char);
                    if word_set.contains(&next[..]) {
                        result
                            .entry(word.as_ref())
                            .or_insert(HashSet::new() as HashSet<&str>)
                            .insert(word_set.get(&next[..]).unwrap());
                    }
                }
            }
        }
        result
    }

    fn dfs<'a>(
        word: &'a str,
        end_word: &str,
        step: u32,
        max_step: u32,
        adjacent: &HashMap<&'a str, HashSet<&'a str>>,
        path: &mut Vec<&'a str>,
        visisted: &mut HashSet<&'a str>,
        result: &mut Vec<Vec<String>>,
    ) {
        if step > max_step {
            return;
        }
        if word.eq(end_word) && step == max_step {
            result.push(path.clone().iter().map(|s| s.to_string()).collect());
        }

        for neighbour in adjacent.get(word).unwrap() {
            if !visisted.contains(*neighbour) {
                visisted.insert(*neighbour);
                path.push(*neighbour);
                Solution::dfs(
                    neighbour,
                    end_word,
                    step + 1,
                    max_step,
                    adjacent,
                    path,
                    visisted,
                    result,
                );
                visisted.remove(*neighbour);
                path.pop();
            }
        }
    }

    fn bfs(begin_word: &str, end_word: &str, adjacent: &HashMap<&str, HashSet<&str>>) -> u32 {
        let mut queue = VecDeque::new();
        queue.push_back(begin_word);
        let mut visisted: HashSet<&str> = HashSet::new();
        let mut found = false;
        let mut step = 0;

        while !queue.is_empty() && !found {
            let curr_level_len = queue.len();
            step += 1;
            for _ in 0..curr_level_len {
                let word = queue.pop_front().unwrap();
                if !visisted.contains(word) {
                    if word.eq(end_word) {
                        found = true;
                        break;
                    }
                    visisted.insert(word);
                    for neighbour in adjacent.get(word).unwrap() {
                        queue.push_back(*neighbour);
                    }
                }
            }
        }

        step
    }

    pub fn find_ladders(
        begin_word: String,
        end_word: String,
        word_list: Vec<String>,
    ) -> Vec<Vec<String>> {
        let mut result = vec![];
        let adjacent = Solution::build_adjacency_list(&word_list, &begin_word);

        let max_step = Solution::bfs(&begin_word, &end_word, &adjacent);
        let mut path = Vec::new();
        path.push(&begin_word[..]);
        let mut visisted = HashSet::new();
        visisted.insert(&begin_word[..]);
        Solution::dfs(
            &begin_word,
            &end_word,
            1,
            max_step,
            &adjacent,
            &mut path,
            &mut visisted,
            &mut result,
        );

        result
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use std::vec;

    use crate::Solution;

    #[test]
    fn test1() {
        assert_eq!(Solution::is_differ_by_a_letter("a", "b"), true);
        assert_eq!(Solution::is_differ_by_a_letter("a", "a"), false);
        assert_eq!(Solution::is_differ_by_a_letter("ab", "ab"), false);
        assert_eq!(Solution::is_differ_by_a_letter("ac", "ab"), true);
    }

    #[test]
    fn test2() {
        let list = vec!["hot", "dot", "dog", "lot", "log", "cog"]
            .iter()
            .map(|s| s.to_string())
            .collect();
        let adj = Solution::build_adjacency_list(&list, "hit");
        assert_eq!(Solution::bfs("hit", "cog", &adj), 5);
    }

    #[test]
    fn test3() {
        let word_list: Vec<String> = vec!["hot", "dot", "dog", "lot", "log"]
            .iter()
            .map(|s| s.to_string())
            .collect();
        assert_eq!(
            Solution::find_ladders("hit".to_string(), "cog".to_string(), word_list.clone()),
            vec![] as Vec<Vec<String>>
        );
    }

    #[test]
    fn test4() {
        let word_list: Vec<String> = vec!["hot", "dot", "dog", "lot", "log", "cog"]
            .iter()
            .map(|s| s.to_string())
            .collect();
        assert_eq!(
            Solution::find_ladders("hit".to_string(), "hit".to_string(), word_list.clone()),
            vec![vec!["hit".to_string()]]
        );
        assert_eq!(
            Solution::find_ladders("hit".to_string(), "hot".to_string(), word_list.clone()),
            vec![vec!["hit".to_string(), "hot".to_string()]]
        );
        assert_eq!(
            Solution::find_ladders("hit".to_string(), "cog".to_string(), word_list.clone()),
            vec![
                vec!["hit", "hot", "dot", "dog", "cog"],
                vec!["hit", "hot", "lot", "log", "cog"],
            ]
        );
    }

    #[test]
    fn test5() {}
}
