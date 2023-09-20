
number_two = 2
for row in range(1, 13):
    for column in range(2, 21):
        print(f"{column:>3} *{row:>3} = {row * column:^2}\t", end=" ")
    print("")
