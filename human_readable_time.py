

"""
Python script to print a given number of seconds duration in an human readable format:
HH:MM:SS
"""


def make_readable(seconds):
    mins = seconds // 60                        # Get amount of mins
    remseconds = seconds % 60                   # Get remainer of seconds / mins
    hours = mins // 60                          # Get amount of hours from mins
    remmins = mins % 60                         # Get remainder of minutes

    return '{:02}:{:02}:{:02}'.format(int(hours), int(remmins), int(remseconds))

print(make_readable(100000))