class TimeMap:
    def __init__(self):
       self.k = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.k: 
            self.k [key] = []
        self.k[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" 
        values = self.k.get(key, [])
        
        l, r = 0, len(values) - 1
        while l <= r: 
            m = (l+r)//2

            if values[m][1] <= timestamp: 
                l = m + 1
                res = values[m][0]
            else: 
                r = m - 1
        return res