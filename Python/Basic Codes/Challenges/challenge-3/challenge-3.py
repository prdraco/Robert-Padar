# Your challenge to create a loan calculator
# Have the user enter the cost of the loan, the interest rate, and 
# the number of years for the loan
# Calculate monthly payments with the following formula
#       M = L[i(1+i)n]/[(1+i)n-1]
# M = monthly payment
# L = Loan amount
# i = interest rate (for an interest rate of 5%, i=0.05)
# n = number of payments
M = 0
i = 0.05
L = float(input('Please enter the loan amount! '))
n = float(input('Please enter how many months you want to borrow! '))

a = 1+i
b = i * a * n
c = a * n - 1
M = (L * b)/c
print('The monthly payments for this loan will be: %.2f ' % M)