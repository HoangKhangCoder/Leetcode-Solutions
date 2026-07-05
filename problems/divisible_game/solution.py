class Solution:
    def divisor(self, x: int):
        div = []
        k = 1
        while k * k <= x:
            if x % k == 0:
                div.append(k)
                if x * x != k:
                    div.append(x // k)
            k += 1
        return div[1:]
        
    def divisibleGame(self, nums: list[int]) -> int:
        maxS = -float("inf")
        minK = float("inf")
        MOD = 10 ** 9 + 7
        uniPrime = {2}
        for num in nums:
            if num in uniPrime:
                continue
            for x in self.divisor(num):
                uniPrime.add(x)
        
        print(uniPrime)
        for k in uniPrime:
            cur = 0
            for x in nums:
                if x % k == 0:
                    cur += x
                else:
                    cur -= x
                if cur > maxS:
                    maxS = cur
                    minK = k
                elif cur == maxS and k < minK:
                    minK = k
                if cur < 0:
                    cur = 0
        return (maxS * minK) % MOD