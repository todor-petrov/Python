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


"""
# 02. Delivery Boy
rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for x in range(rows)]
start_position = [(r, c) for r in range(rows) for c in range(cols) if matrix[r][c] == 'B']
start_row, start_col = start_position[0][0], start_position[0][1]
row, col = start_row, start_col
while True:
    moves = {'up': [row - 1, col], 'down': [row + 1, col],
             'left': [row, col - 1], 'right': [row, col + 1]}
    way = input()
    next_row, next_col = moves[way][0], moves[way][1]

    if not 0 <= next_row < rows or not 0 <= next_col < cols:
        matrix[start_row][start_col] = ' '
        print('The delivery is late. Order is canceled.')
        break
    if matrix[next_row][next_col] == '*':
        continue
    if matrix[next_row][next_col] == 'A':
        matrix[row][col] = '.'
        matrix[next_row][next_col] = 'P'
        matrix[start_row][start_col] = 'B'
        print('Pizza is delivered on time! Next order...')
        break
    if matrix[next_row][next_col] == 'P':
        matrix[row][col] = '.'
        row, col = next_row, next_col
        matrix[next_row][next_col] = 'R'
        print('Pizza is collected. 10 minutes for delivery.')
        continue
    if matrix[row][col] != 'R':
        matrix[row][col] = '.'
    row, col = next_row, next_col
    matrix[row][col] = '.'

for start_row in matrix:
    print(''.join(start_row))
"""
