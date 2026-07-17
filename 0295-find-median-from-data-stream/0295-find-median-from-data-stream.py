import bisect
class MedianFinder:

    def __init__(self):
        self.length = 0
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2:
            return self.nums[self.length // 2]
        res = (self.nums[self.length // 2] + self.nums[self.length // 2 - 1]) / 2
        return res


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()