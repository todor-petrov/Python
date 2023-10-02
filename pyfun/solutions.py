# 01. Pythagorean tripe
correct_triples_count = 0
for c in range(1, 48):
    for b in range(1, c):
        for a in range(1, b):
            if a ** 2 + b ** 2 == c ** 2:
                correct_triples_count += 1
                print('{}, {}, {}'.format(a, b, c))
print(correct_triples_count)