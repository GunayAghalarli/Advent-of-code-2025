f = open('day2.txt', 'r')
ordered_list = []

for line in f:
    numbers_list = list(map(int, line.split()))
    
    if numbers_list == sorted(numbers_list) or numbers_list == sorted(numbers_list, reverse=True):
        valid = True  
        for j in range(len(numbers_list) - 1):
            if abs(numbers_list[j] - numbers_list[j + 1]) > 3 or numbers_list[j] == numbers_list[j + 1]:  
                break  
        
        if valid:  
            ordered_list.append(numbers_list)  

print('ordered_list', len(ordered_list))
