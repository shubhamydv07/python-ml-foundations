numbers = [3, 8, 1, 7, 4, 9, 2]

for i in range(len(numbers)):
    if numbers[i] == 7:
        print('Found 7! , at index',i)
        break
else:
        print('Not Found')