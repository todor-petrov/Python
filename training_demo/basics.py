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


"""
# 04. Game Number Wars
first_player, second_player = input(), input()
first_player_points, second_player_points = 0, 0
winner, points = '', 0
number_wars = False
command = input()
while command != 'End of game':
    first_player_card = int(command)
    second_player_card = int(input())
    points = abs(first_player_card - second_player_card)
    if first_player_card > second_player_card:
        first_player_points += points
    elif second_player_card > first_player_card:
        second_player_points += points
    else:
        number_wars = True
        first_player_card = int(input())
        second_player_card = int(input())
        difference = abs(first_player_card - second_player_card)
        if first_player_card > second_player_card:
            winner = first_player
            points = first_player_points
        else:
            winner = second_player
            points = second_player_points
        break
    command = input()
if number_wars:
    print('Number wars!')
    print(f'{winner} is winner with {points} points')
else:
    winner = first_player if first_player_points > second_player_points else second_player
    points = first_player_points if first_player_points > second_player_points else second_player_points
    print(f'{first_player} has {first_player_points} points\n'
          f'{second_player} has {second_player_points} points')
"""


"""
# 04. Darts
initial_points = 301
points = {'Single': 1, 'Double': 2, 'Triple': 3}
won_the_leg, successful_shots, unsuccessful_shots = False, 0, 0
player, command = input(), input()
while command != 'Retire':
    score = int(input()) * points[command]
    if initial_points - score == 0:
        successful_shots += 1
        won_the_leg = True
        break
    elif initial_points - score > 0:
        successful_shots += 1
        initial_points -= score
    else:
        unsuccessful_shots += 1
    command = input()
if won_the_leg:
    print(f'{player} won the leg with {successful_shots} shots.')
else:
    print(f'{player} retired after {unsuccessful_shots} unsuccessful shots.')
"""


"""
# 05. Tennis Ranklist
from math import floor

tournaments, initial_points = int(input()), int(input())
points = {'W': 2000, 'F': 1200, 'SF': 720}
wins, total_points = 0, initial_points
for tournament in range(tournaments):
    kind_of_tournament = input()
    total_points += points[kind_of_tournament]
    if kind_of_tournament == 'W':
        wins += 1
average_points = (total_points - initial_points) / tournaments
tournaments_won_percent = (wins / tournaments) * 100
print(f'Final points: {total_points}\n'
      f'Average points: {floor(average_points)}\n'
      f'{tournaments_won_percent:.2f}%')
"""


"""
# 05. Fitness Center
visitors = int(input())
activities = {'Back': 0, 'Chest': 0, 'Legs': 0, 'Abs': 0, 'Protein shake': 0, 'Protein bar': 0}
for visitor in range(visitors):
    activity = input()
    activities[activity] += 1
for k, v in activities.items():
    print(f'{v} - {k.lower()}')
trainers = sum(activities[k] for k, v in activities.items() if 'Protein' not in k)
trainers_percentage = (trainers / visitors) * 100
buyers = sum(activities[k] for k, v in activities.items() if 'Protein' in k)
buyers_percentage = (buyers / visitors) * 100
print(f'{trainers_percentage:.2f}% - work out\n'
      f'{buyers_percentage:.2f}% - protein')
"""


"""
# High Jump
target_height = int(input())
current_height = target_height - 30
failed_jumps_counter, failed_workout = 0, False
jumps_counter = 0

jump = int(input())
while jump != '':
    jumps_counter += 1
    if jump > current_height:
        if current_height >= target_height:
            break
        current_height += 5
        failed_jumps_counter = 0
    elif jump <= current_height:
        failed_jumps_counter += 1
        if failed_jumps_counter == 3:
            failed_workout = True
            break
    jump = int(input())
if not failed_workout:
    print(f'Tihomir succeeded, he jumped over {current_height}cm after {jumps_counter} jumps.')
else:
    print(f'Tihomir failed at {current_height}cm after {jumps_counter} jumps.')
"""


"""
# 06. Basketball Tournament
matches_won, matches_lost = 0, 0
matches_counter = 0
tournament = input()
while tournament != 'End of tournaments':
    matches = int(input())
    matches_counter += matches
    for match in range(1, matches + 1):
        desi_team_points, other_team_points = int(input()), int(input())
        difference = abs(desi_team_points - other_team_points)
        if desi_team_points > other_team_points:
            matches_won += 1
            print(f'Game {match} of tournament {tournament}: win with {difference} points.')
        else:
            matches_lost += 1
            print(f'Game {match} of tournament {tournament}: lost with {difference} points.')
    tournament = input()
matches_won_percent = matches_won / matches_counter * 100
matches_lost_percent = matches_lost / matches_counter * 100
print(f'{matches_won_percent:.2f}% matches win\n'
      f'{matches_lost_percent:.2f}% matches lost')
"""