counter = 0
number = range(1, 51, 2)
for count in number:
    # counter += 1
    count += 1
    print(count, end=" ")
    counter += 1
    average = count / counter
print(average)
# even = []
# for count in range(0, 51, 2):
#     even.append(count)
# print(even)
# average = sum(even) / len(even)
#
# print(average)