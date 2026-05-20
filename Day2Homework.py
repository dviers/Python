## Homework Day 2
## Date: 2026-05-19
## Author: Dave V
## Daily Deliverable (The Bill Splitter): A standalone script that prompts for a
## total cost and number of contributors, executes explicit float and integer conversions,
## and yields a perfectly formatted output message.

total_cost = float(input("What is the total cost?: "))
num_contributors = int(input("How many contributors?: "))
split_amount = total_cost / num_contributors
print(f"The total cost is ${total_cost:,.2f}")
print(f"There are {num_contributors} contributors")
print(f"Each contributor owes ${split_amount:,.2f}")
