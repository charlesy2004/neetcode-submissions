class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_cnt = 0
        for i in range(k):
            if blocks[i] == 'W':
                w_cnt += 1
        res = w_cnt

        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                w_cnt -= 1
            if blocks[i] == 'W':
                w_cnt += 1
            res = min(w_cnt, res)
        return res