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