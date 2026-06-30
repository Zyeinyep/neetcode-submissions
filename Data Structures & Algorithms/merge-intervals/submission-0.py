class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merge = []
        for s,e in intervals:
            if not merge or merge[-1][1] < s:
                merge.append([s,e])
            else:
                merge[-1][1] = max(merge[-1][1], e)
        return merge
        