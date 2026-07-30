from heapq import heappush, heappop

class Twitter:

    def __init__(self):
        self.followMap = {}      
        self.tweetMap = {}          
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []

        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        ans = []

        users = [userId]
        if userId in self.followMap:
            users.extend(self.followMap[userId])

        for user in users:
            if user in self.tweetMap:
                idx = len(self.tweetMap[user]) - 1
                time, tweetId = self.tweetMap[user][idx]
                heappush(heap, (-time, tweetId, user, idx))

        while heap and len(ans) < 10:
            negTime, tweetId, user, idx = heappop(heap)
            ans.append(tweetId)

            if idx > 0:
                idx -= 1
                time, tweetId = self.tweetMap[user][idx]
                heappush(heap, (-time, tweetId, user, idx))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
            
        if followerId not in self.followMap:
            self.followMap[followerId] = set()

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)