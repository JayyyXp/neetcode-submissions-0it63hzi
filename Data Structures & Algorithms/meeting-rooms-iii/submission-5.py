class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [0] * n  # stores when each room becomes free
        timesUsed = [0] * n

        for meetingStart, meetingEnd in meetings:
            duration = meetingEnd - meetingStart
            scheduled = False

            # First, try to assign the meeting to a free room (available at or before meetingStart)
            for i in range(n):
                if rooms[i] <= meetingStart:
                    rooms[i] = meetingEnd
                    timesUsed[i] += 1
                    scheduled = True
                    break

            if not scheduled:
                # No rooms are free — find the room that becomes free the earliest
                earliest_index = min(range(n), key=lambda i: rooms[i])
                wait_time = rooms[earliest_index]
                rooms[earliest_index] = wait_time + duration
                timesUsed[earliest_index] += 1
            print(rooms)
        return timesUsed.index(max(timesUsed))
  