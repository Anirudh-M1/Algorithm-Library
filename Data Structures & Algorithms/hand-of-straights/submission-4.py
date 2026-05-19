class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        possibleHands = len(hand) / groupSize
        if possibleHands % 1 != 0: 
            return False
        
        freq =Counter(hand)


        heap = list(freq.keys())
        heapq.heapify(heap)
        hands = 0
        print(freq)
        while True:
            print(f"Hand Number {hands} and freqs: {freq}")
            
            if hands == possibleHands:
                return True

            while heap and freq[heap[0]] == 0:
                print(f"the Heap is: {heap}") 
                heapq.heappop(heap)
            
            if heap:
                print(heap)
                start = heap[0]
                print(start)
            else:
                return False 
            print(f"group Size is {groupSize}")

            for i in range(groupSize): 
                print(f"current number {[start + i]} and its freq {freq[start + i]}")
                if freq[start + i] == 0: 
                    return False
                else:
                    freq[start + i] -= 1

            hands +=1


