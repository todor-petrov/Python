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


"""
# 03. Gymnastics
data = {
        'Russia':   {'ribbon': 18.500, 'hoop': 19.100, 'rope': 18.600},
        'Bulgaria': {'ribbon': 19.000, 'hoop': 19.300, 'rope': 18.900},
        'Italy':    {'ribbon': 18.700, 'hoop': 18.900, 'rope': 18.850},
}
max_points = 20
country, apparatus = input(), input()
percent = (max_points - data[country][apparatus]) / max_points * 100
total_points = data[country][apparatus]
print(f'The team of {country} get {total_points:.3f} on {apparatus}.\n'
      f'{percent:.2f}%')
"""


"""
# 03. World Snooker Championship
stage, ticket_type, tickets, photo = (input(), input(), int(input()), input())
prices = {'Quarter final': {'Standard':  55.50, 'Premium': 105.20, 'VIP': 118.90},
          'Semi final':    {'Standard':  75.88, 'Premium': 125.22, 'VIP': 300.40},
          'Final':         {'Standard': 110.10, 'Premium': 160.66, 'VIP': 400.00}}
mid_price = prices[stage][ticket_type] * tickets
total_price = 0
if mid_price > 4000:
    total_price += 0.75 * mid_price
elif mid_price > 2500:
    total_price += 0.90 * mid_price
else:
    total_price = mid_price
if mid_price <= 4000 and photo == 'Y':
    total_price += tickets * 40
print(f'{total_price:.2f}')
"""
