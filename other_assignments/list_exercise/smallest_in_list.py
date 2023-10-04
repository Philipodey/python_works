numbers = [15, 20, 25, 20, 10, 5]
smallest_one = numbers[5]
print(smallest_one)

smallest = 0

for i in numbers:
    if i < smallest:
        smallest = i

print(smallest)
