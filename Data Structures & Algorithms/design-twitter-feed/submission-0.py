from heapq import heappush, heappop, heapify

class Twitter(object):

    def __init__(self):
        self.followMap = defaultdict(set) #userid - following
        self.tweetMap = defaultdict(list) #userid - list of tweets
        self.time = 0


    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetMap[userId].append([self.time,tweetId])
        self.time -= 1 #python max heap

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        heap = []
        for fl in self.followMap[userId] |{userId}:
            tweets = self.tweetMap[fl]
            idx = len(self.tweetMap[fl]) - 1 #idx of most recent tweet by user
            if idx >= 0:
                time, tweetid = tweets[idx]
                heappush(heap, (time,tweetid,fl,idx))
        
        while heap and len(res) < 10:
            time,tweetid,fl,idx = heappop(heap)
            res.append(tweetid)

            #next most recent tweet by user just popped
            if idx >= 1:
                time2, tweetid2 = self.tweetMap[fl][idx-1]
                heappush(heap,(time2,tweetid2,fl,idx-1))
        return res
    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)