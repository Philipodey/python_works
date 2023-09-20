passes = 0
failures = 0
number = int(input("Enter result (1=pass, 2=fail): "))
count = 0
while number != -1:
    if passes != 1:
        print(int(input("Enter result (1=pass, 2=fail): ")))
    elif failures != 2:
        print(int(input("Enter result (1=pass, 2=fail): ")))
    elif passes == 1:
       passes += 1
    elif failures == 2:
        failures += 1
    count += 1
print("passes:", passes)
print("failures:", failures)
if passes > 8:
    print("Bonus to instructor")