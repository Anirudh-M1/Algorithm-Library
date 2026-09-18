class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): 
            return ""
        
        tprof = Counter(t)
        wprof = defaultdict(int)
        
        bestlen, bestL, bestR = float("inf"), 0, 0
        left, missing = 0, len(tprof)
        
        for right, ch in enumerate(s):
            if ch not in tprof:
                continue
            
            wprof[ch] += 1
            if ch in tprof and wprof[ch] == tprof[ch]: 
                missing -= 1
            
            while missing == 0: 
                if right - left + 1 < bestlen: 
                    bestlen = right - left + 1 
                    bestL = left
                    bestR = right 
                
                lch = s[left]
                if lch in tprof:
                    if tprof[lch] == wprof[lch]: 
                        missing += 1
                    wprof[lch] -= 1
                left += 1

        return s[bestL:bestR + 1] if bestlen != float("inf") else ""
