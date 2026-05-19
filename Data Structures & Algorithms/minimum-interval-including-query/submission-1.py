class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()  # sort by start
        ans = []
        for query in queries:
            ans.append(self.binarySearch(intervals, query))
        return ans
    
    def binarySearch(self, intervals, query):
        left = 0
        right = len(intervals) - 1

        # Find the rightmost interval whose start <= query
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] <= query:
                left = mid + 1
            else:
                right = mid - 1

        # Scan backward from right to 0 — do NOT break on end < query
        minSize = float("inf")
        for i in range(right, -1, -1):
            start, end = intervals[i]
            if start <= query <= end:
                minSize = min(minSize, end - start + 1)

        return minSize if minSize != float("inf") else -1
