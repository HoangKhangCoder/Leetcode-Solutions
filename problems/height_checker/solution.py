class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        length = len(heights)
        # This one is in the Bubble Sort Chapter, you can use .sort() or sorted() instead.
        def bubbleSort(nums: List[int], length) -> List[int]:
            n = length - 1
            hasSorted = False
            while not hasSorted:
                hasSorted = True
                for i in range(n):
                    if nums[i] > nums[i + 1]:
                        hasSorted = False
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
            return nums
        
        sortedHeights = bubbleSort(copy.deepcopy(heights), length)

        cnt = 0
        for i in range(length):
            cnt += (sortedHeights[i] != heights[i])
        return cnt