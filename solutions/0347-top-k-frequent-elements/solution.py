class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = Counter(nums)
        for key,val in counts.items():
            heapq.heappush(heap,(val,key))
        while len(heap)>k:
            heapq.heappop(heap)
        return [value for key,value in heap]
