#Expenses#
rent = int(input("enter monthly rent payment: "))
groceries = int(input("enter monthly grocerie bill: "))
phone = int(input("enter monthly phone bill: "))
entertainment = int(input("enter monthly entertainment: "))
subscriptions = int(input("enter total monthly subscription costs: "))
transportation = int(input("enter total transportation costs: "))
total_expense = rent + groceries + phone + entertainment + entertainment + subscriptions + transportation
#Active Income#
job_income = int(input("enter monthly income from your job: "))
job2_income = int(input("enter your monthly income from your second job: "))
active_income = job_income + job2_income
#Passive Income#
dividend_income = int(input("enter average monthly dividend: "))
x = round((total_expense/active_income) * 100, 2)
#High Interest Debt >5%(priority 1)#
credit_card = int(input("enter the amount owing on your credit card: "))
line_of_credit = int(input("enter the amount owing on your line of credit: "))
high_interest_debt = credit_card + line_of_credit
if high_interest_debt > 0:
    print("\nFirst priority to pay off credit cards and lines of credit.")
else:
    pass
#Emergency Fund#
emergency_fund = int(input("enter how much you have in an emergency fund: "))
if emergency_fund < (3 * total_expense):
    print("\nThis is where you want to put your money before anything else ")
else:
    pass
#Savings#
#Surplus#
surplus  = active_income - total_expense

print(f"\n\nYour total monthly expenses are {total_expense}, which is {x}% of your active income.")
print(f"\nYou passive income streams adds an additional {dividend_income} per month.")
print(f"\nThis month you have an extra {surplus}, which can be utilized to produce lasting wealth.")

if surplus >= 0:
    print(f"\nYou got money to use! Congradulations!")


