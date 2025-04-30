def calculate_debt_free_time_with_interest(loan_amount, monthly_repayment, interest_rate):
    """
    Calculate how long it takes to become debt-free with an interest rate.

    :param loan_amount: The initial loan amount (in kr).
    :param monthly_repayment: The amount repaid each month (in kr).
    :param interest_rate: The monthly interest rate (as a decimal, e.g., 0.01 for 1%).
    :return: The number of months needed to become debt-free.
    """
    if monthly_repayment <= 0:
        raise ValueError("Monthly repayment must be greater than 0.")
    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than 0.")
    if interest_rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    months = 0
    while loan_amount > 0:
        loan_amount += loan_amount * interest_rate  # Add interest
        loan_amount -= monthly_repayment  # Subtract repayment
        months += 1

        if loan_amount < 0:  # If overpaid, stop
            loan_amount = 0

    return months


# Example usage
n = int(input("Enter the loan amount (kr): "))
x = int(input("Enter the monthly repayment amount (kr): "))
r = float(input("Enter the annual interest rate for a whole year  / bye 12 (as a decimal, e.g., 0.0025 for 3%): "))

months_needed = calculate_debt_free_time_with_interest(n, x, r)
print(f"You will be debt-free in {months_needed/12} year.")