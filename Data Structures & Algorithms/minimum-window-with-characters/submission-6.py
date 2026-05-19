class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": 
            return ""
        
        #small
        countT = Counter(t)
        #string 
        countS = {}

        left = 0
        have = 0
        need = len(countT)

        minChars = float("inf")
        ans = ""
        for right, char in enumerate(s): 
            print(s[left:right +1])

            if char in countT: 
                countS[char] = countS.get(char, 0) + 1

                if countS[char] == countT[char]: 
                    have+=1
                    print(f"Have incremented for char {char} , have {have}, need {need}")
                    print(f"countS {countS}, countT {countT}")


            while have == need: 
                if right - left + 1 < minChars:
                    ans = s[left :right + 1]
                    minChars = len(ans)


                #increment left pointer
                if s[left] in countT: 
                    countS[s[left]] -= 1  
                    if countS[s[left]] < countT[s[left]]: 
                        have -=1 
                left+=1

        return ans


