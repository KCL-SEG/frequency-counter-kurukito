"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = dict()
    count = 0
    while count < items.length:
        current = items[count]
        if isinstance(current,str) != True:
            current = str(items[count])
        i = 0
        while i < len(frequencies):
            frequencies.add(count(i))
    return frequencies
    print(frequencies)

