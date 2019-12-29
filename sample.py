# Comment
# Hello World

'''
hello
world
'''

"""
hello
world
"""

def meeting_rooms(intervals):
    intervals.sort(key=lambda x:x[0])
    for i in range(1, len(intervals)):
        if intervals[i-1][1] > \ # indent
		intervals[i][0]:
            return False
    return True

print(meeting_rooms([[0, 1], [2,3], [4,6]]))
# [[0, 1], [2,5], [4,6]]

# i          :2
# in[i-1]    :[2,5]
# in[i]      :[4,6]
