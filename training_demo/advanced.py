from collections import deque

armors = deque([int(x) for x in input().split(',')])
strikes = [int(x) for x in input().split(',')]
killed_monsters = 0

while armors and strikes:
    armor, strike = armors.popleft(), strikes.pop()
    if strike >= armor:
        killed_monsters += 1
        strike -= armor
        if strike != 0:
            if strikes:
                strikes[-1] += strike
            else:
                strikes.append(strike)
    else:
        armor -= strike
        armors.append(armor)
if not armors:
    print('All monsters have been killed!')
if not strikes:
    print('The soldier has been defeated.')
print(f'Total monsters killed: {killed_monsters}')