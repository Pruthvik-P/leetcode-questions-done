class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        heap = []

        for word in words:
            freq[word] += 1
        
        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))

        return [heapq.heappop(heap)[1] for _ in range(k)]
