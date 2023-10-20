"""
# 01. Monster Extermination
from collections import deque

monsters_armors = deque([int(x) for x in input().split(',')])
soldier_strikes = [int(x) for x in input().split(',')]
killed_monsters = 0

while monsters_armors and soldier_strikes:
    armor, strike = monsters_armors.popleft(), soldier_strikes.pop()
    if strike >= armor:
        killed_monsters += 1
        strike -= armor
        if strike != 0:
            if soldier_strikes:
                soldier_strikes[-1] += strike
            else:
                soldier_strikes.append(strike)
    else:
        armor -= strike
        monsters_armors.append(armor)
if not monsters_armors:
    print('All monsters have been killed!')
if not soldier_strikes:
    print('The soldier has been defeated.')
print(f'Total monsters killed: {killed_monsters}')
"""



# 02. Delivery Boy
rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for x in range(rows)]
print(matrix)