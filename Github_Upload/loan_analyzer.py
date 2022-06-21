# coding: utf-8
import csv
from pathlib import Path

# define a list of loans of varying costs

loan_costs = [500, 600, 200, 1000, 450]

# find the length of the list of loans and store it in a new variable length_loan_costs, print the result

length_loan_costs = len(loan_costs)
print(length_loan_costs)
# Result: 5

# find the total of all the loans in the list using the sum() function

total_loan_costs = sum(loan_costs)
print(total_loan_costs)
# Result: 2750

# find the average loan in the list by dividing the total_loan_cost variable by the length_loan_cost variable and then print the result

average_loan_amount = total_loan_costs / length_loan_costs
print(average_loan_amount)
# Result: 550.0

# the following dictionary stores data for a loan with different values related to the price, rem months, repayment interval, and future value

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# store the future value and remaining months for the loan into new variables using the get() function on the dictionary
# print the results for these variables

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(future_value, remaining_months)
# Results: 1000, 9


# using a discount rate of 20% (0.2) we calculate the fair value of the loan and store it into a new variable fair_value
# the fair value can be calculated using the equation: Future Value / (1 + Discount_Rate/12) ** remaining_months
# print the resulting fair value of the loan

discount_rate = 0.2
fair_value = future_value / (1 + discount_rate/12) ** remaining_months
print(fair_value)
# Result: 861.77

# define the variable loan_cost as the "loan_price" value in the loan dictionary
loan_cost = loan.get("loan_price")

# define present_value as equal to fair_value so they can be used interchangeably
present_value = fair_value

# to determine if the loan should be taken based on its fair value we use a conditional if/else statement to see if the present value is greater
# than the loan cost
# if the loan cost is greater than the fair value we will tell the investor not to purchase the loan
if present_value >= loan_cost:
    print(f"It is worthwhile to buy the loan, as the value: {present_value} is greater than the cost: {loan_cost}")
else: 
    print(f"Do not buy the loan as the cost: {loan_cost} is greater than the value: {present_value}")

# the following dictionary represents the data and values for a new loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# we create a function to determine the fair/present value of the loan by passing the parameters that we will later fill using data from the new_loan dictionary

def calculate_present_value (future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    print(f"The present value of the loan is: {present_value}")

# define the annual discount rate in a variable called annual_discount_rate

annual_discount_rate = 0.2

# call the calculate_present_value function we created 
# we use the get() function to populate the parameters with data from the new_loan dictionary when we call our function

calculate_present_value(new_loan.get("future_value"), new_loan.get("remaining_months"), annual_discount_rate)

# loans defines a list of dictionaries housing data for various loans, there are 4 objects in the list
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# inexpensive_loans will be appended later, but it must first be defined as a blank list
inexpensive_loans = []

# use a for loop in the loans list to get the loan price and check if the loans are inexpensive ie. they cost less than or equal to $500
# if a loan is determined to be inexpensive we append the empty inexpensive_loans list we created
for loan in loans:
    loan_price = loan.get("loan_price")
    if loan_price <= 500:
        inexpensive_loans.append(loan)

# print the list of inexpensive loans
print(inexpensive_loans)

# Set the output header to a list corresponding to what we find in the body of the data
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path for the new .csv file that will be created 
output_path = Path("./inexpensive_loans.csv")

# use the with open() function to write a csv file to the path we just specified. 
# create an instance of the csv.writer() function and call it loans_writer
# the delimiter is ' ' because the data is separated by spaces
# use the loans_writer object to writerow() the header data
# then use a for-loop to write the data underneath the header in the new .csv file

with open(output_path, 'w', newline='') as csvfile:
    loans_writer = csv.writer(csvfile, delimiter=' ')
    loans_writer.writerow(header)
    for loan in inexpensive_loans:
        loans_writer.writerow(loan.values())
