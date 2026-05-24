class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_dict = {}
        for num in nums:
            c_dict[num] = 1 + c_dict.get(num, 0)
        freq = [[] for i in range(len(nums) + 1)]
        for key,v in c_dict.items():
            freq[v].append(key)
        alist = []
        for i in range(len(freq) - 1,0, -1):
            for num in freq[i]:
                alist.append(num)
                if len(alist) == k:
                    return alist
        return alist