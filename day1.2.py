f = open('day1.txt', 'r')
data = f.read()
numbers_list = list(map(int, data.split()))

left = []
right = []
count = 0
result = []

for i, x in enumerate(numbers_list):
    if i% 2 == 0:
        right.append(x)
    else:
        left.append(x)

for r_elem in right:
    count = left.count(r_elem)  
    if count > 0: 
        print(count)
        res = r_elem * count  
        result.append(res)

print("Result:", sum(result))
