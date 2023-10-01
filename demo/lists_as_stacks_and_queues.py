"""
01. Reverse Numbers

def reverse_numbers(numbers):
    print(' '.join(numbers[::-1]))


reverse_numbers([x for x in input().split(' ')])
"""


"""
02. Stacked Queries

def stacked_queries():
    stack, integer = [], int(input())
    for _ in range(integer):
        query = input().split(' ')
        if query[0] == '1':
            stack.append(int(query[1]))
        elif query[0] == '2' and stack:
            stack.pop()
        elif query[0] == '3' and stack:
            print(max(stack))
        elif query[0] == '4' and stack:
            print(min(stack))
    stack_for_return = stack[::-1]
    print(', '.join(str(x) for x in stack_for_return))


stacked_queries()
"""


"""
03. Fast Food

from collections import deque

available_quantity, orders = int(input()), deque([int(x) for x in input().split(' ')])
not_enough_food = False
print(max(orders))
while orders:
    if available_quantity >= orders[0]:
        available_quantity -= orders.popleft()
    else:
        not_enough_food = True
        break
if not_enough_food:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")
else:
    print('Orders complete')
"""


"""
04. Fashion Boutique

clothes, rack_capacity = [int(x) for x in input().split(' ')], int(input())
racks_number, current_rack_capacity = 1, rack_capacity
while clothes:
    if clothes[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes.pop()
    else:
        current_rack_capacity = rack_capacity
        racks_number += 1
        current_rack_capacity -= clothes.pop()
print(racks_number)
"""