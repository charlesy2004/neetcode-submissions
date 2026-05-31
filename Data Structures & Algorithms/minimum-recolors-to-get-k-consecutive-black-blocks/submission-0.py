class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        num_black = 0
        i = 0
        j = 0
        min_op = len(blocks)
        while i + k <= len(blocks):
            curr_op = 0
            j = 0
            while j < k:
                if blocks[i + j] != 'B':
                    curr_op += 1
                j += 1
            if curr_op < min_op:
                min_op = curr_op
            i += 1
        return min_op
            