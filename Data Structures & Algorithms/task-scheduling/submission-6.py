class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        waitQueue = deque() # freq remaining, time until ready
        tasksFreq = list(Counter(tasks).values())
        negTasksFreq = [-f for f in tasksFreq] 

        heapq.heapify(negTasksFreq)
        time = 0

        while (waitQueue or negTasksFreq) :
            print(f"CURRENT TIME {time}")
            print(f"waitlist is {waitQueue}")
            print(f"taskFreq is {negTasksFreq}")

            if waitQueue and waitQueue[0][1] == time: 
                freq, _ = waitQueue.popleft()
                heapq.heappush(negTasksFreq, freq)

            if negTasksFreq:
                curFreq = heapq.heappop(negTasksFreq) 
                curFreq+= 1
                if curFreq != 0:
                    waitQueue.append([curFreq, time+n + 1])
            time += 1
        return time        