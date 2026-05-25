class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.tm[key]
        l, r =0 , len(arr) - 1
        
        val = ""

        while l <= r:   
            mid = (l+r)//2
            if timestamp < arr[mid][0]: 
                r = mid - 1
            elif timestamp > arr[mid][0]: 
                val = arr[mid][1]
                l = mid + 1
            else: 
                return arr[mid][1]
        
        return val 