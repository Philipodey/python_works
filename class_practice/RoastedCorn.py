picture = [
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    print()
    for column in row:
        if column == 0:
            print(' ', end=' ')
        else:
            print("*", end=' ')

