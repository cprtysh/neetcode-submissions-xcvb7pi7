class TimeMap:

    def binS(self, val, t):
        start, end = 0, len(val) - 1
        ans = -1

        while start <= end:
            mid = (start + end) // 2

            if val[mid][1] <= t:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans

    def __init__(self):
        self.base = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.base:
            self.base[key] = []

        self.base[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.base:
            return ""

        index = self.binS(self.base[key], timestamp)

        if index == -1:
            return ""

        return self.base[key][index][0]