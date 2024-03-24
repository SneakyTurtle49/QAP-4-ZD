#description
#author Zac Davidge
#date: 3/21/24

#imports

import datetime
from datetime import datetime, timedelta

#default values for the program

DEFAULT_VALUES = {
    "next_policy_number": 1944,
    "basic_premium": 869.00,
    "discount_additional_cars": 0.25,
    "cost_extra_liability": 130.00,
    "cost_glass_coverage": 86.00,
    "cost_loaner_car": 58.00,
    "HST_rate": 0.15,
    "processing_fee": 39.99
}

#lists used for validating inputs

VALID_PROVINCES = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]
PAYMENT_METHODS = ["Full", "Monthly", "Down Pay"]


#first function used to validate the input for province so that it must be in the list

def validate_province(province):
    return province in VALID_PROVINCES

#second function to calc the premium cost including extra charges

def calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    premium = DEFAULT_VALUES["basic_premium"]
    for num_cars in range(2, num_cars + 1):
        premium += DEFAULT_VALUES["basic_premium"] * (1 - DEFAULT_VALUES["discount_additional_cars"])
    if extra_liability == "yes":
        premium += DEFAULT_VALUES["cost_extra_liability"] * num_cars
    if glass_coverage == "yes":
        premium += DEFAULT_VALUES["cost_glass_coverage"] * num_cars
    if loaner_car == "yes":
        premium += DEFAULT_VALUES["cost_loaner_car"] * num_cars
    return premium

#third function to calculate the total cost

def calculate_total_cost(premium, payment_method, down_payment=0):
    total_cost = premium + (premium * DEFAULT_VALUES["HST_rate"])
    if payment_method == "Monthly":
        total_cost += DEFAULT_VALUES["processing_fee"]
        monthly_cost = (total_cost - down_payment) / 8
        return total_cost, monthly_cost
    return total_cost, None

#fourth function to get valid inputs from the user and return them for calcs

def get_valid_input(prompt, valid_options,):

    prompt; ("enter 'yes' or 'no': ").lower()
    valid_options = ["yes", "no"]

    user_input = input(prompt).lower()
    while user_input not in valid_options:
        print("Error: please enter one of the following options ('yes' or 'no')")
        user_input = input(prompt).lower()
    return user_input

#fifth function to calc additional cost

def calculate_additional_costs(num_cars, extra_liability, glass_coverage, loaner_car):
    additional_costs = 0
    if extra_liability == 'yes':
        additional_costs += DEFAULT_VALUES["cost_extra_liability"] * num_cars
    if glass_coverage == 'yes':
        additional_costs += DEFAULT_VALUES["cost_glass_coverage"] * num_cars
    if loaner_car == 'yes':
        additional_costs += DEFAULT_VALUES["cost_loaner_car"] * num_cars
    return additional_costs

#sixth function to print the receipt

def print_receipt(customer_info, policy_info, premium_details, claims_list):
  
    #Prints a formatted receipt with customer and policy details, premium calculations, and previous claims.

    #Header

    print("One Stop Insurance Company")
    print("Customer Insurance Policy Receipt")
    print("---------------------------------")
    
    #Customer Information

    print("Customer Information:")
    for key, value in customer_info.items():
        print(f"{key.title()}: {value}")
    
    #Policy Information
        
    print("\nPolicy Details:")
    for key, value in policy_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    #Premium Calculations
        
    print("\nPremium Calculations:")
    for key, value in premium_details.items():
        if isinstance(value, float):  # Format floats to two decimal places
            print(f"{key.replace('_', ' ').title()}: ${value:.2f}")
        else:
            print(f"{key.replace('_', ' ').title()}: {value}")
    
    #Previous Claims
            
    if claims_list:
        print("\nPrevious Claims:")
        print("Claim #    Claim Date   Amount")
        print("---------------------------------")
        for claim in claims_list:
            print(f"{claim['Claim Number']}   {claim['Claim Date']}   ${claim['Amount']:.2f}")
    
    #Footer
            
    print("---------------------------------")
    print("Thank you for choosing One Stop Insurance Company.")    

#main loop for customer inputs

while True:

#initialize dictionaries

    customer_info = {}

    policy_info = {}

    premium_details = {}

    #populate customer info

    customer_info['first_name'] = input("Enter customer first name: ").title()
    customer_info['last_name'] = input("Enter customer last name: ").title()   
    customer_info['address'] = input("Enter customer address: ")
    customer_info['city'] = input("Enter customer city: ").title()
    customer_info['postal_code'] = input("Enter customer postal code: ")
    customer_info['phone_num'] = input("Enter customer phone number: ")

    while True:
        province = input("Enter customer province (XX): ").upper()
        if province == "":
            print("Error: cannot be blank.")
        elif len(province) != 2:
            print("Error: must be 2 characters only.")
        elif province not in VALID_PROVINCES:
            print("Error: invalid province.")
        else:
            customer_info['Province'] = province
            break

    #populate policy info

    num_cars = int(input("How many cars being insured? "))
    policy_info['number of cars'] = num_cars

    #initialize down payment

    down_payment = 0

    while True:
        payment_method = input("Enter payment method (Full or Monthly or Down Pay): ").title()
        if payment_method == "":
            print("Error: cannot be blank.")
        elif payment_method not in PAYMENT_METHODS:
            print("Error: invalid payment method.")
        else:
            policy_info['payment method'] = payment_method

        if payment_method == "Monthly":
            number_of_months = input("Enter the number of months you would like to finance for: ")
            policy_info['number of months'] = number_of_months
            break
        elif payment_method == "Down Pay":
            down_payment = float(input("Enter the down payment amount: "))
            policy_info['down payment'] = down_payment
            break
        else:
            break
    

    while True:
        extra_liability = get_valid_input("Enter 'yes' or 'no' for extra liability coverage: ", ['yes', 'no'])
        print(f"Extra Liability Coverage: {extra_liability}")
        policy_info['extra liability'] = extra_liability
        break


    while True:
        glass_coverage = get_valid_input("Enter 'yes' or 'no' for glass coverage: ", ['yes', 'no'])
        print(f"Glass Coverage: {glass_coverage}")
        policy_info['glass coverage'] = glass_coverage
        break

    while True:
        loaner_car = get_valid_input("Enter 'yes' or 'no' for Loaner Car coverage: ", ['yes', 'no'])
        print(f"Loaner Car Coverage: {loaner_car}")
        policy_info['loaner car'] = loaner_car
        break

    #calc premium

    premium = calculate_premium(num_cars, extra_liability, glass_coverage, loaner_car)

    #calc total cost and monthly payment

    total_cost, monthly_payment = calculate_total_cost(premium, payment_method, down_payment)

    #calc premium details

    premium_details['Premium'] = premium
    premium_details['Total Cost'] = total_cost
    if payment_method == 'Monthly':
        premium_details['Monthly Payment'] = monthly_payment
    else:
        premium_details['Monthly Payment'] = 'N/A'

    additional_costs = calculate_additional_costs(num_cars, extra_liability, glass_coverage, loaner_car)
    premium_details['Additional Costs'] = additional_costs

    total_premium_before_tax = premium + additional_costs

    hst_amount = total_premium_before_tax * DEFAULT_VALUES["HST_rate"]

    total_cost_after_tax = total_premium_before_tax + hst_amount

    #populate premium_details

    premium_details['Premium'] = premium
    premium_details['Total Cost'] = total_cost
    premium_details['Monthly Payment'] = monthly_payment if payment_method == 'Monthly' else 'N/A'
    premium_details['Additional Costs'] = additional_costs
    premium_details['Total Premium Before Tax'] = total_premium_before_tax
    premium_details['HST Amount'] = hst_amount
    premium_details['Total Cost After Tax'] = total_cost_after_tax

     #check if value is a float to properly format

    for key, value in premium_details.items():
        if isinstance(value, float):
            print(f"{key}: ${value:,.2f}")
        else:
            print(f"{key}: {value}")

    #claims list

    claims_list = []
    while True:
        add_claim = input("Do you want to add a claim? (yes/no): ").lower()
        if add_claim == 'no':
            break
        claim_num = input("Enter claim number: ")
        claim_date = input("Enter the date of claim (YYYY-MM-DD): ")
        claim_amount = total_cost_after_tax
        claims_list.append({'Claim Number': claim_num, 'Claim Date': claim_date, 'Amount': claim_amount})

    #Call the function to print the receipt
    
    print_receipt(customer_info, policy_info, premium_details, claims_list)

    #check if the user wants to add another customer

    continue_prompt = input("Enter another customer? (yes/no): ").lower()
    if continue_prompt != 'yes':
        break
