class Twitter:

    def __init__(self):
        self.userToTweets = defaultdict(list) # list of (time, tweetId)
        self.userToFollow = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToTweets[userId].append((self.time, tweetId))
        self.time += 1 # because we will use a max-heap

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        all_tweets.extend(self.userToTweets[userId])
        for follow in self.userToFollow[userId]:
            if follow != userId:
                all_tweets.extend(self.userToTweets[follow])
        print(all_tweets)
        print()
        recent_10 = []
        for tweet in all_tweets:
            heapq.heappush(recent_10, tweet)
            if len(recent_10) == 11:
                popped = heapq.heappop(recent_10)
                print("popped: " + str(popped))
        
        return [tweetId for _, tweetId in sorted(recent_10)[::-1]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToFollow[followerId]:
            self.userToFollow[followerId].remove(followeeId)        
