class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for c in tasks:
            freq[c] = 1 + freq.get(c, 0)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        time = 0
        while max_heap:
            used = []
            for _ in range(n+1):
                if max_heap:
                    count = heapq.heappop(max_heap)
                    count += 1
                    if count < 0:
                        used.append(count)
                time += 1
                if not max_heap and not used:
                    break
            for count in used:
                heapq.heappush(max_heap, count)
        return time


