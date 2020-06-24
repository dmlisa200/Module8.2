"""
program:  assign_average.py
author:  Lisa Kilmer
last date modified:  6-23-2020
This program is a case/switch in python.  A switcher is a dictionary that can map
cases to their functionality.
"""

def switch_average(i):

    switcher = {
        'A': 'Ankeny',
        'B': 'Ames',
        'C': 'Waukee',
        'D': 'Grimes',
        'E': 'Des Moines',
    }
    print(switcher.get(i, "Invalid town name"))

if __name__ == '__main__':
    switch_average('D')
