class Twitter:
    from collections import defaultdict
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) #id -> all the tweets that user posted [cnt, tweetid]
        self.followMap = defaultdict(set) #id -> all the people that user follows 

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        #print(f"**User {userId} Posted {tweetId}**")
        self.count +=1 
        self.tweetMap[userId].append([self.count, tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        #print(f"**Retrieving Feed for User {userId}**")
        self.followMap[userId].add(userId)
        newsFeed = []
        posterIdxs = {}

        for poster in self.followMap[userId]:
              posterIdxs[poster] = len(self.tweetMap[poster]) - 1
        # print(f"tweetMap: {self.tweetMap}")
        # print(f"followMap: {self.followMap}")
        # print(f"posterIdx {posterIdxs}")

        for _ in range(10): 
            maxCnt = float("-inf")
            mostRecentTweetId = None
            mostRecentPoster = None
            for poster in self.followMap[userId]:
                posterIndex = posterIdxs[poster]
                posterTweets = self.tweetMap[poster]
                
                if posterIndex >= 0 and posterTweets[posterIndex][0] > maxCnt: 
                    maxCnt =  posterTweets[posterIndex][0]
                    mostRecentTweetId = posterTweets[posterIndex][1]
                    mostRecentPoster = poster

            if mostRecentTweetId != None: 
                newsFeed.append(mostRecentTweetId)
                posterIdxs[mostRecentPoster] -= 1
        
        #print(f"**Feed: {newsFeed}**")
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        #print(f"**User {followerId} Followed {followeeId}**")
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #print(f"**User {followerId} Un-Followed {followeeId}**")
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
