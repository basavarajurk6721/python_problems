principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in percentage): "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100
print(f"Simple Interest: {simple_interest}")

total_amount = principal + simple_interest
print(f"Total Amount after {time} years: {total_amount}")