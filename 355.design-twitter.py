from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.following: dict[int, set[int]] = defaultdict(set)
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        min_heap: list[tuple[int, int, int, int]] = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if self.tweets[followeeId]:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                min_heap.append((time, followeeId, tweetId, index - 1))
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            _, followeeId, tweetId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(min_heap, (time, followeeId, tweetId, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
