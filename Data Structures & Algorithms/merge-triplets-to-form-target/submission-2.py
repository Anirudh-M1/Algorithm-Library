class Solution:
    from collections import defaultdict
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        validTriplets = []
        mergeFound = [False] * 3
        for triplet in triplets:
            validTriplet = True
            for idx, val in enumerate(triplet): 
                if val > target[idx]:
                    validTriplet = False

            if validTriplet: 
                for idx, val in enumerate(triplet):
                    if target[idx] == val: 
                        mergeFound[idx] = True

        for b in mergeFound: 
            if b == False: 
                return False
        return True 
        
        return True