# Your challenge is to calculate shipping charges for a shopper
# Ask the user to enter the amount for their total purchase
# If their total is under £50 add £10, otherwise shipping cost is free
# Tell the user their final total including shipping costs and format 
# the number so it looks like a monetary value

total = float(input('Please, enter your total purchase: '))
if total < 50:
    total = total + 10
    print('Your shipping fee takes an extra £10 ')
    print('Your total purchase including shipping charges: \
        £%.2f ' % total)
else:
    print('Your shipping is free of charge! ')
    print('Your total purchase including shipping charges: \
        £%.2f ' % total)
print('Have a nice day!')
