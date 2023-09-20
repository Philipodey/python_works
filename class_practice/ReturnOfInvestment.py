# investment_amount = int(input("Enter any amount: "))
# for count in range(1, 31):
#     money_increase = investment_amount
#     investment_percentage = 0.10
#     money_increase *= investment_percentage
#     investment_amount += money_increase
#     print(f"Your ROI is {money_increase:.2f}, Your investment is now {investment_amount:.2f} in  year {count} ")

investment_amount = int(input("Enter any amount: "))
count = 1
while count <= 30:
    money_increase = investment_amount
    investment_percentage = 0.10
    money_increase *= investment_percentage
    investment_amount += money_increase
    print(f"Your ROI is {money_increase:.2f}, Your investment is now {investment_amount:.2f} in year {count}")
    count += 1
