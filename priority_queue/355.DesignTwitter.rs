use std::collections::{BinaryHeap, HashMap, HashSet};

struct Twitter {
    user_tweets: HashMap<i32, Vec<(u32, i32)>>,
    user_followees: HashMap<i32, HashSet<i32>>,
    tweet_count: u32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Twitter {
    fn new() -> Self {
        Twitter {
            user_tweets: HashMap::new(),
            user_followees: HashMap::new(),
            tweet_count: 0,
        }
    }

    fn post_tweet(&mut self, user_id: i32, tweet_id: i32) {
        self.user_tweets
            .entry(user_id)
            .or_insert(vec![])
            .push((self.tweet_count, tweet_id));
        self.tweet_count += 1;
    }

    fn get_news_feed(&mut self, user_id: i32) -> Vec<i32> {
        // tweet_count, tweet_id, next tweet index
        let mut heap: BinaryHeap<(u32, i32, i32, usize)> = BinaryHeap::new();
        let mut res: Vec<i32> = Vec::new();

        self.user_followees.entry(user_id).or_insert(HashSet::new()).insert(user_id);

        if let Some(followees) = self.user_followees.get(&user_id) {
            for followee in followees.iter() {
                if let Some(tweets) = self.user_tweets.get(followee) {
                    if let Some(last_tweet) = tweets.last() {
                        let (tweet_count, tweet_id) = last_tweet;
                        let next_index = (tweets.len() - 1) - 1;
                        heap.push((*tweet_count, *tweet_id, *followee, next_index));
                    }
                }
            }
        }

        loop {
            if heap.is_empty() || res.len() == 10 {
                break;
            }

            if let Some(item) = heap.pop() {
                let (_tweet_count, tweet_id, tweet_user_id, next_idx) = item;
                res.push(tweet_id);

                if let Some(tweets) = self.user_tweets.get(&tweet_user_id) {
                    if let Some((tweet_count, tweet_id)) = tweets.get(next_idx) {
                        heap.push((*tweet_count, *tweet_id, tweet_user_id, next_idx - 1));
                    }
                }
            }
        }

        res
    }

    fn follow(&mut self, follower_id: i32, followee_id: i32) {
        self.user_followees
            .entry(follower_id)
            .or_insert(HashSet::new())
            .insert(followee_id);
    }

    fn unfollow(&mut self, follower_id: i32, followee_id: i32) {
        if let Some(set) = self.user_followees.get_mut(&follower_id) {
            set.remove(&followee_id);
        }
    }
}