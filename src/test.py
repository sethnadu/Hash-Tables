array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

least_sum = 0

for i in range(len(array)):
    least = array[i][0]
    print(least)
    for j in array[i]:
        
        if j < least:
            least = j
    least_sum += least
        
print("sum", least_sum)

