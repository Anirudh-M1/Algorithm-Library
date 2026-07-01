class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ct = Counter(arr1)
        s2 = set(arr2)
        left = []
        right = []
        for n in arr1:
            if n not in s2:
                right.append(n)
        
        for n in arr2:
            for _ in range(ct[n]):
                left.append(n)
        
        right.sort()
        ans = left + right

        return ans
            