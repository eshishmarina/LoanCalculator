import math
import argparse

parser = argparse.ArgumentParser(description="This program is a loan payment calculator.")
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--interest')
parser.add_argument('--periods')
parser.add_argument('--payment')
args = parser.parse_args()

args_type = args.type
args_interest = args.interest
args_loan_principal = args.principal
args_num_of_periods = args.periods
args_annuity = args.payment

if args_type == 'annuity':
    if args_annuity is None \
            and args_loan_principal is not None \
            and args_num_of_periods is not None \
            and args_interest is not None:

        loan_principal = int(args_loan_principal)
        num_of_periods = int(args_num_of_periods)
        interest = float(args_interest)
        nominal_interest = interest / 12 / 100
        annuity = math.ceil(
            loan_principal *
            (nominal_interest * math.pow(1 + nominal_interest, num_of_periods)) /
            (math.pow(1 + nominal_interest, num_of_periods) - 1))

        print(f'Your monthly payment = {annuity}!')

    elif args_loan_principal is None \
            and args_num_of_periods is not None \
            and args_annuity is not None \
            and args_interest is not None:

        annuity = float(args_annuity)
        num_of_periods = int(args_num_of_periods)
        interest = float(args_interest)
        nominal_interest = interest / 12 / 100
        loan_principal = math.ceil(
            annuity /
            (nominal_interest * math.pow(1 + nominal_interest, num_of_periods) /
             (math.pow(1 + nominal_interest, num_of_periods) - 1)))

        print(f'Your loan principal = {loan_principal}!')
        print(f'Overpayment = {num_of_periods * annuity - loan_principal}')

    elif args_num_of_periods is None \
            and args_loan_principal is not None \
            and args_annuity is not None \
            and args_interest is not None:

        loan_principal = int(args_loan_principal)
        annuity = float(args_annuity)
        interest = float(args_interest)
        nominal_interest = interest / 12 / 100
        log_number = annuity / (annuity - nominal_interest * loan_principal)
        log_base = 1 + nominal_interest
        num_of_periods = math.ceil(math.log(log_number, log_base))

        if num_of_periods < 12:
            print(f'It will take {num_of_periods} months to repay this loan!')

        elif num_of_periods == 12:
            print('It will take 1 year to repay this loan!')

        elif num_of_periods > 12:
            years = num_of_periods // 12
            months = num_of_periods - 12 * years
            print(f'It will take {years} years and {months} months to repay this loan!')
        print(f'Overpayment = {num_of_periods * annuity - loan_principal}')

    else:
        print("Incorrect parameters")

elif args_type == 'diff' \
        and args_num_of_periods is not None \
        and args_loan_principal is not None \
        and args_interest is not None:

    num_of_periods = int(args_num_of_periods)
    loan_principal = int(args_loan_principal)
    interest = float(args_interest)
    sum_ = 0

    for i in range(1, num_of_periods + 1):
        diff_payment = loan_principal / num_of_periods + \
                       interest / 12 / 100 * \
                       (loan_principal - loan_principal * (i - 1) / num_of_periods)
        diff_payment = math.ceil(diff_payment)
        print(f'Month {i}: payment is {diff_payment}')
        sum_ += diff_payment

    print(f'Overpayment = {sum_ - loan_principal}')

else:
    print('Incorrect parameters')
