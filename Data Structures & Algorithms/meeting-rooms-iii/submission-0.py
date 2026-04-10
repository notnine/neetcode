import heapq
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # first intuition: run min heap meetings 2 algo, but keep track of how many meetings each room has had

        def get_start_time(meeting: List[int]) -> int:
            return meeting[0]
        
        meetings.sort(key=get_start_time)
        ongoing_meetings = [] # ongoing meetings sorted by end time decr. contains tuples of (end time, start time, room)
        free_rooms = [i for i in range(n)] # min heap of free rooms
        heapq.heapify(free_rooms)
        room_to_used = defaultdict(int) # room_to_used[i] is how many times room i has been used

        for meeting in meetings:
            
            # clear out meetings that's ended
            while ongoing_meetings and ongoing_meetings[0][0] <= meeting[0]:
                popped_meeting = heapq.heappop(ongoing_meetings)
                heapq.heappush(free_rooms, popped_meeting[2])
            
            # if no free rooms, delay curr meeting
            if not free_rooms:
                # get the meeting that's ending soonest, delay curr meeting to start after this one
                soonest_ending_meeting = heapq.heappop(ongoing_meetings)
                smallest_avail_room = soonest_ending_meeting[2]
                curr_meeting_len = meeting[1] - meeting[0]
                meeting = [soonest_ending_meeting[0], soonest_ending_meeting[0] + curr_meeting_len]
            else:
                smallest_avail_room = heapq.heappop(free_rooms)
            
            heapq.heappush(ongoing_meetings, (meeting[1], meeting[0], smallest_avail_room))
            room_to_used[smallest_avail_room] += 1
        
        # get most used room
        most_used_room_freq = 0
        for room in room_to_used:
            most_used_room_freq = max(most_used_room_freq, room_to_used[room])
        
        for room in room_to_used:
            if room_to_used[room] == most_used_room_freq:
                return room