class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)

        if n < 10:
            return []

        seen = set()
        repeated = set()

        window = s[:10]
        seen.add(window)

        for i in range(10, n):
            window = window[1:] + s[i]

            if window in seen:
                repeated.add(window)
            else:
                seen.add(window)

        return list(repeated)