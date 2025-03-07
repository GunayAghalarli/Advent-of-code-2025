f = open('day1.txt', 'r')
data = f.read()
numbers_list = list(map(int, data.split()))

left = []
right = []

for i, x in enumerate(numbers_list):
    if i% 2 == 0:
        right.append(x)
    else:
        left.append(x)


right.sort()
left.sort()

difference = []
for a, b in zip(right, left):
    difference.append((a - b))
result = [abs(x) for x in difference]
print(len(result))
print(sum(result))