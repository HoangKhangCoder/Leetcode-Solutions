class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Walk through string s and compress it into consecutive runs of the
        # same character. Convention used in "runs":
        #   - A run of all '1's: stored as a positive length (count of consecutive '1' chars).
        #   - A run of all '0's: stored as a negative length (to distinguish it from a '1' run).
        runs = []
        oneRun = 0   # length of the '1' run currently being scanned (positive number)
        zeroRun = 0  # length of the '0' run currently being scanned (stored as a negative number)
        totalOnes = 0     # total count of '1' characters in s
        runCount = 0      # number of runs collected so far

        for char in s:
            if char == "0":
                zeroRun -= 1
                # If a '1' run was being tracked, it has just ended,
                # so push it into the list of runs and reset it.
                if oneRun > 0:
                    runs.append(oneRun)
                    runCount += 1
                oneRun = 0
            else:
                # If a '0' run was being tracked, it has just ended,
                # so push it into the list of runs and reset it.
                if zeroRun < 0:
                    runs.append(zeroRun)
                    runCount += 1
                oneRun += 1
                totalOnes += 1
                zeroRun = 0

        # Push the final run (not yet pushed inside the loop) into the list.
        runs.append([zeroRun, oneRun][int(s[-1])])
        runCount += 1

        # The minimum possible result is doing no trade at all -> the current count of '1's.
        maxActive = totalOnes

        # We want to find two '0' runs (at indices i and i+2) with a '1' run
        # in between them (index i+1). A "trade" lets us flip these two '0'
        # runs into '1's, joining them through the middle '1' run, in order
        # to maximize the total number of active '1' characters.
        for i in range(runCount - 2):
            # Skip if runs[i] is a '1' run (positive value) since we need
            # to start from a '0' run (negative value).
            if runs[i] > 0:
                continue
            activeCount = abs(runs[i]) + abs(runs[i + 2]) + totalOnes
            maxActive = max(maxActive, activeCount)

        return maxActive
