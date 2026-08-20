"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.end)
        prev = -float("inf")
        for curr in intervals:
            if prev > curr.start:
                return False
            prev = curr.end
        return True

