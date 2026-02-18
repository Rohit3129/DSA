class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def Nxtvalchar(str, index):
            backspace = 0
            while index >=0:
                if backspace == 0 and str[index] != "#":
                    break
                elif str[index] == "#":
                    backspace += 1
                else:
                    backspace -= 1
                index -= 1
            return index
        Is = len(s) - 1
        It = len(t) - 1
        while Is >=0 or It >=0:
            Is = Nxtvalchar(s, Is)
            It = Nxtvalchar(t, It)
            ch_s = s[Is] if Is >= 0 else ""
            ch_t = t[It] if It >= 0 else ""
            if ch_s != ch_t:
                return False
            Is -= 1
            It -= 1
        return True