"""
# 01. Tennis Equipment

from math import floor, ceil

racquet_price = float(input())
racquet_number = int(input())
trainers_number = int(input())
trainers_price = racquet_price / 6

racquets_and_trainers_price = racquet_price * racquet_number + trainers_price * trainers_number
other_equipment = racquets_and_trainers_price * 0.2
total_price = racquets_and_trainers_price + other_equipment
player_price = floor(total_price / 8)
sponsors_price = ceil(total_price * 7 / 8)
print(f'Price to be paid by Djokovic {player_price}')
print(f'Price to be paid by sponsors {sponsors_price}')
"""

"""
# 01. Basketball Equipment

annual_fee = int(input())
trainers = annual_fee * 0.6
equipment = trainers * 0.8
ball = equipment / 4
accessories = ball / 5
total_price = sum([annual_fee, trainers, equipment, ball, accessories])
print(f'{total_price:.2f}')
"""


"""
# 02. Football Results
games = [[int(x) for x in input().split(':')],
         [int(x) for x in input().split(':')],
         [int(x) for x in input().split(':')]]
wins, loses, equal = 0, 0, 0
for game in games:
    if game[0] > game[1]:
        wins += 1
    elif game[0] < game[1]:
        loses += 1
    else:
        equal += 1
print(f'Team won {wins} games.\n'
      f'Team lost {loses} games.\n'
      f'Drawn games: {equal}')
"""


"""
# 02. Skeleton
control_time = int(input()) * 60 + int(input())
length, seconds_100_m = float(input()), int(input())
decreased_time = (length / 120) * 2.5
player_time = (length / 100) * seconds_100_m - decreased_time
if player_time <= control_time:
    print(f'Marin Bangiev won an Olympic quota!\n'
          f'His time is {player_time:.3f}.')
else:
    print(f'No, Marin failed! He was {(player_time - control_time):.3f} second slower.')
"""
