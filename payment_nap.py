import math

print("""What do you want to calculate?
type "n" for the number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
user_input = input("> ")

if user_input == "n":
    print("Enter the loan principal:")
    loan_principal = int(input("> "))

    print("Enter the monthly payment:")
    monthly_pay = int(input("> "))

    print("Enter the loan interest:")
    loan_interest = float(input("> "))

    nom_interest = loan_interest / (12 * 100)
    number_months = math.ceil(math.log((monthly_pay / (monthly_pay - nom_interest * loan_principal)), 1 + nom_interest))
    years = number_months // 12
    months = number_months % 12

    if years == 0:
        if months > 1:
            print(f"It will take {months} months to repay this loan!")
        else:
            print(f"It will take {months} month to repay this loan!")
    elif months == 0:
        if years > 1:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} year to repay this loan!")
    else:
        if years > 1 and months > 1:
            print(f"It will take {years} years and {months} months to repay this loan!")
        elif years == 1 and months == 1:
            print(f"It will take {years} year and {months} month to repay this loan!")
        elif years > 1 and months == 1:
            print(f"It will take {years} years and {months} month to repay this loan!")
        elif years == 1 and months > 1:
            print(f"It will take {years} year and {months} month to repay this loan!")

elif user_input == "a":
    print("Enter the loan principal:")
    loan_principal = int(input("> "))

    print("Enter the number of periods:")
    periods = int(input("> "))

    print("Enter the loan interest:")
    loan_interest = float(input("> "))

    nom_interest = loan_interest / (12 * 100)
    annuity = math.ceil(loan_principal * ((nom_interest * math.pow(1 + nom_interest, periods)) / (math.pow(1 + nom_interest, periods) - 1)))

    print(f"Your monthly payment = {annuity}!")

elif user_input == "p":
    print("Enter the annuity payment:")
    annuity = float(input("> "))

    print("Enter the number of periods:")
    periods = int(input("> "))

    print("Enter the loan interest:")
    loan_interest = float(input("> "))

    nom_interest = loan_interest / (12 * 100)
    loan_principal = round(annuity / ((nom_interest * math.pow(1 + nom_interest, periods)) / (math.pow(1 + nom_interest, periods) - 1)))

    print(f"Your loan principal = {loan_principal}!")
