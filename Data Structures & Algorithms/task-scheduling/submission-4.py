class Solution:
    import heapq
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskHash = defaultdict(int)
        for t in tasks:
            taskHash[t] +=  1 

        taskFreq = list(Counter(tasks).items())
        taskFreq = [(-n,c) for c,n in taskFreq]
        heapq.heapify(taskFreq)

        cooldownQueue = deque()
        secs = 0

        while taskFreq or cooldownQueue: 
            if taskFreq:
                freq, char = heapq.heappop(taskFreq)
                if freq + 1 < 0: 
                    cooldownQueue.append((secs + n, char, freq + 1))

            if cooldownQueue and cooldownQueue[0][0] <= secs: 
                _, c, f = cooldownQueue.popleft()
                heapq.heappush(taskFreq, (f, c))
 
            secs+=1 

        return secs
        

        
        
