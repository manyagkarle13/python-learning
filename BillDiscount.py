'''Write a program that asks for a bill amount and applies this rule:

If bill > 1000 → 10% discount

If bill > 500 → 5% discount

Else → No discount'''
bill_Amount=float(input("Enter the amount of bill : "))
if bill_Amount>1000:
    discount=bill_Amount*10/100
    total_Bill=bill_Amount-discount
    print(f"The total bill got the discount of 10%")
    print(f"The total bill is {total_Bill}")
elif bill_Amount>500:
    discount=bill_Amount*5/100
    total_Bill=bill_Amount-discount
    print(f"The total bill got the discount of 5%")
    print(f"The total bill is {total_Bill}")
else:
    print(f"The total bill is {bill_Amount} and no discount applied ,Thank You!")    