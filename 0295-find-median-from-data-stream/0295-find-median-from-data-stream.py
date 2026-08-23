import bisect

class MedianFinder:
    # Idea: maintain an array that's always kept sorted. Every time a new
    # number is added, insert it at the correct position using binary
    # search (bisect.insort), so the array stays sorted at a cost of O(n)
    # per insertion, while looking up the median only takes O(1).

    def __init__(self):
        self.length = 0
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)  # insert num at the correct position to keep the array sorted
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2:
            # Odd number of elements: the median is the single middle element
            return self.nums[self.length // 2]
        # Even number of elements: the median is the average of the two middle elements
        res = (self.nums[self.length // 2] + self.nums[self.length // 2 - 1]) / 2
        return res


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()