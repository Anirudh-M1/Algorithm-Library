class Solution:
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        roundsRemaining = n
        heap = []

        taskHash = defaultdict(int)
        for t in tasks:
            taskHash[t] +=  1 

        taskFreq = list(taskHash.items())

        taskFlopped = [(-n,c) for c,n in taskFreq]
        
        heapq.heapify(taskFlopped)

        cooldown = {}
        cooldownQueue = []
        secs = 0

        while taskFlopped or cooldownQueue: 
            print(f"taskFlopped: {taskFlopped}")
            print(f"cooldownQueue: {cooldownQueue}")

            if taskFlopped:
                freq, char = heapq.heappop(taskFlopped)
                print(f"Character: {char}, Remaining: {freq}")
                if freq + 1 < 0: 
                    cooldownQueue.append((secs + n, char, freq + 1))

            if cooldownQueue and cooldownQueue[0][0] <= secs: 
                _, c, f = cooldownQueue.pop(0)
                heapq.heappush(taskFlopped, (f, c))
 
            secs+=1 


        return secs
        
        

        
        
