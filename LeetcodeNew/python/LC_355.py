
"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""


import collections

class Twitter:
    def __init__(self):

        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)
        self.order = 0

    def postTweet(self, userId, tweetId):

        self.tweets[userId] += (self.order, tweetId),
        self.order -= 1

    def getNewsFeed(self, userId):
        res = []
        for i in self.following[userId] | {userId}:
            for tw in self.tweets[i]:
                res.append(tw)
        res = sorted(res)[:10]
        return [news for i, news in res]

    def follow(self, followerId, followeeId):

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):

        self.following[followerId].discard(followeeId)




twitter = Twitter()
twitter.follow(1,2)
twitter.follow(1,3)
twitter.follow(1,4)
twitter.follow(1,5)

twitter.postTweet(2, 22)
twitter.postTweet(3, 33)
twitter.postTweet(4, 44)
twitter.postTweet(5, 55)


print(twitter.getNewsFeed(1))



