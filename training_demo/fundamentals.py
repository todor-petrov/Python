"""
# 01. Computer Store
price_without_taxes = 0
line = input()
while line not in ['special', 'regular']:
    price = float(line)
    if price < 0:
        print('Invalid price!')
    else:
        price_without_taxes += price
    line = input()
if price_without_taxes == 0:
    print('Invalid order!')
else:
    taxes = price_without_taxes * 0.2
    print(f'Congratulations you\'ve just bought a new computer!\n'
          f'Price without taxes: {price_without_taxes:.2f}$\n'
          f'Taxes: {taxes:.2f}$\n'
          f'-----------')
    total_price = price_without_taxes + taxes
    if line == 'special':
        total_price *= 0.90
    print(f'Total price: {total_price:.2f}$')
"""


"""
# 02. The Lift
people, wagons = int(input()), [int(x) for x in input().split(' ')]
max_wagon_volume = 4
for wagon in range(len(wagons)):
    free_seats = max_wagon_volume - wagons[wagon]
    if people and free_seats:
        if people < free_seats:
            wagons[wagon] += people
            people = 0
        else:
            wagons[wagon] += free_seats
            people -= free_seats
free_seats = sum([max_wagon_volume - wagon for wagon in wagons])
if free_seats > 0:
    print(f'The lift has empty spots!')
if people > 0:
    print(f"There isn\'t enough space! {people} people in a queue!")
print(f"{' '.join(str(w) for w in wagons)}")
"""


"""
# 03. Memory Game
elements = [x for x in input().split()]
moves, game_won = 0, False
command = input()
while command != 'end':
    moves += 1
    i, j = [int(x) for x in command.split()]
    if i == j or not 0 <= i <= len(elements) - 1 or not 0 <= j <= len(elements) - 1:
        middle = int(len(elements) / 2)
        first_part = elements[:middle]
        middle_part = [f'-{moves}a', f'-{moves}a']
        last_part = elements[middle:]
        elements = first_part + middle_part + last_part
        print('Invalid input! Adding additional elements to the board')
    elif elements[i] == elements[j]:
        removed_element = elements[i]
        elements = [x for x in elements if x != removed_element]
        print(f'Congrats! You have found matching elements - {removed_element}!')
    else:
        print('Try again!')
    if not elements:
        game_won = True
        break
    command = input()
if game_won:
    print(f'You have won in {moves} turns!')
else:
    print(f"Sorry you lose :(\n"
          f"{' '.join(x for x in elements)}")
"""
