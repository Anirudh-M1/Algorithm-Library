class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # planning: go over all triplets, 
        # the value in target must be max in that col our of all otherwise it will be killed in the merges

        mergedTriplets = [False] * 3

        for triplet in triplets:
            validTriplet = True
            for index, val in enumerate(triplet):
                if val > target[index]: 
                    validTriplet = False
                
            if validTriplet:
                for index, val in enumerate(triplet):
                    if target[index] == val:
                        mergedTriplets[index] = True
            
        return all(mergedTriplets)