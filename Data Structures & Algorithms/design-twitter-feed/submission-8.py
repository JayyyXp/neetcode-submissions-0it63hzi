class Twitter:

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.follows = collections.defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = list(self.tweets[userId])

        for following in self.follows[userId]:
            if following != userId:
                for tweet in self.tweets[following]:
                    tweets.append(tweet)

        #print(tweets)
        tweets.sort(key=lambda x: -x[0])

        return [ tweet[1] for tweet in tweets[:10]]
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId in self.follows) and (followeeId in self.follows[followerId]): 
            self.follows[followerId].remove(followeeId)
        
