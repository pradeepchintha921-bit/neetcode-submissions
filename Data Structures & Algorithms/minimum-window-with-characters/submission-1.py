class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        countS = {}

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("inf")

        left = 0

        for right in range(len(s)):
            c = s[right]
            countS[c] = countS.get(c, 0) + 1

            if c in countT and countS[c] == countT[c]:
                have += 1

            while have == need:
                # Update answer
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = [left, right]

                # Remove left character
                leftChar = s[left]
                countS[leftChar] -= 1

                if leftChar in countT and countS[leftChar] < countT[leftChar]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""