"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return True

        prev = None
        for i in intervals:
            if prev == None:
                prev = i.end
                continue
            if prev > i.start:
                return False
            prev = i.end
        return True
            
            

    
        
        

            
