

# for count in range(1, 50):
#     if count % 3 == 0 and count % 5 == 0:
#         print("FizzBuzz")
#     elif count % 3 == 0:
#         print("Fizz")
#     elif count % 5 == 0:
#         print("Buzz")
#     else:
#         print(count)
count = 1
while count < 50:
    if count % 3 ==0 and count % 5 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count += 1