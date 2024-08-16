from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        array = [(arr_id, arrays[arr_id][0], arrays[arr_id][-1]) for arr_id in range(len(arrays))]
        mins = sorted(array, key=lambda item: item[1])[:2]
        maxs = sorted(array, key=lambda item: item[2], reverse=True)[:2]
        if mins[0][0] == maxs[0][0]:
            return max(maxs[1][2] - mins[0][1],maxs[0][2] - mins[1][1])
        return maxs[0][2] - mins[0][1]
