class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            freq = {}
            freqCount ={}

            for j in range(i, n):
                x = nums[j]
                oldFreq = freq.get(x, 0)

                if oldFreq > 0:
                    freqCount[oldFreq] -= 1
                    if freqCount[oldFreq] == 0:
                        del freqCount[oldFreq]

                freq[x] = oldFreq + 1
                freqCount[freq[x]] = freqCount.get(freq[x], 0) +1

                length = j -i + 1

                if len(freq) == 1:
                    ans = max(ans, length)
                elif len(freqCount) == 2:
                    keys = sorted(freqCount.keys())
                    small, large = keys[0], keys[-1]
                    if large == 2 * small:
                        ans = max(ans, length)
        return ans
