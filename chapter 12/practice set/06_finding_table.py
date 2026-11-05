result = []

for i in range(1, 1000):
    row = [i * j for j in range(1, 11)]  # table of i: i*1 to i*11
    # Check if digit '2' appears anywhere in the full table
    if not any('2' in str(x) for x in row):
        result.append(i)

print(result)
           







        