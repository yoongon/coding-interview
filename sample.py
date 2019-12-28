# For example,
# Given [ [0, 30], [5, 10], [15, 20] ],
# return false.

# [0, 30], [5, 10], [15, 20]
# [0, 1] , [2, 3], [4,5]
# [0, 1] , [2, 5], [4, 6]

# sort based on start
# previous end is greater than current start => return False


def meeting_rooms(intervals):
    intervals.sort(key=lambda x:x[0])
    print ("asdf")
    for i in range(1, len(intervals)):
        if intervals[i-1][1] > intervals[i][0]:
            return False
    return True

print(meeting_rooms([[0, 1], [2,3], [4,6]]))
# [[0, 1], [2,5], [4,6]]

# i          :2
# in[i-1]    :[2,5]
# in[i]      :[4,6]