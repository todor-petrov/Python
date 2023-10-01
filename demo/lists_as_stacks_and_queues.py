'''
01.Reverse Numbers

def reverse_numbers(numbers):
    print(' '.join(numbers[::-1]))


reverse_numbers([x for x in input().split(' ')])
'''

'''
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
'''

