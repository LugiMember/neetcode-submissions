"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        times = []
        for interval in intervals:
            start = interval.start
            end = interval.end
            times.append((start, 1))
            times.append((end, -1))

        times.sort()
        count = 0
        largest = 0
        for time in times:
            count += time[1]
            if count > largest:
                largest = count

        return largest
            
        