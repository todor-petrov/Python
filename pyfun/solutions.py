# 01. Pythagorean tripe
"""
correct_triples_count = 0
for c in range(1, 48):
    for b in range(1, c):
        for a in range(1, b):
            if a ** 2 + b ** 2 == c ** 2:
                correct_triples_count += 1
                print('{}, {}, {}'.format(a, b, c))
print(correct_triples_count)
"""


# 02. Heap's algorithm
import sys

"""
def generate_permutations(a, n):
    if n == 0:
        print(''.join(a))
    else:
        for i in range(n):
            generate_permutations(a, n - 1)
            j = 0 if n % 2 == 0 else i
            a[j], a[n] = a[n], a[j]
        generate_permutations(a, n - 1)


if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word = sys.argv[1]

generate_permutations(list(word), len(word) - 1)
"""


"""
# 03.
import sys, re

counts = {}
for line in sys.stdin:
    for word in re.findall(r'[a-z\']+', line.lower()):
        counts[word] = counts.get(word, 0) + 1
        for word, count in sorted(counts.items()):
            print(word, count)
"""