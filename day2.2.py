with open('day2.txt', 'r') as f:
    ordered_list = []

    for line in f:
        numbers_list = list(map(int, line.split()))

        for i in range(len(numbers_list)):
            new_list = numbers_list[:i] + numbers_list[i+1:]  
            
            if new_list == sorted(new_list) or new_list == sorted(new_list, reverse=True):
                valid = True 
                
                for j in range(len(new_list) - 1):
                    if abs(new_list[j] - new_list[j + 1]) > 3 or new_list[j] == new_list[j + 1]:  
                        valid = False  
                        break  

                if valid:  
                    ordered_list.append(numbers_list)  
                    break  
print('ordered_list', len(ordered_list))
