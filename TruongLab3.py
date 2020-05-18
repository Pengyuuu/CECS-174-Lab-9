import math

#ask user for taxable income
tax_income = float(input('What is your 2018 taxable income?: '))

#calculate their taxable income
if (tax_income > 10000000.0):
    taxable = tax_income - 500000.00
    taxable = taxable * .37
    taxable += 150689.50
    new_tax = ((((9500000) * .37) + 150689.50) + (tax_income -10000000) * .7)
    

elif (tax_income > 38700.00 and tax_income <= 82500.00):
    taxable = tax_income - 38700.00
    taxable = taxable * 0.22
    taxable += 4453.50

elif (tax_income > 9525.00 and tax_income <= 38700.00):
    taxable = tax_income - 9525.00
    taxable = taxable * 0.12
    taxable += 952.50

elif (tax_income >= 0.0 and tax_income <= 9525.00):
    taxable = tax_income - 0.0
    taxable = taxable * 0.1

#find tax rates
tax_rate = taxable / tax_income
tax_rate = tax_rate * 100

if (tax_income > 10000000.0):
    new_taxrate = new_tax / tax_income


print('Your tax liability is $', format(taxable, ',.2f'))
print('Your effective tax rate is', format(tax_rate, ',.1f'),'%')
print()

if (tax_income > 10000000.0):
    print('With a new 70% bracket, your tax liability would be $', format(new_tax, ',.2f'))
    print('Your effective tax rate with the new bracket would be', format(new_taxrate, '.1%'))

#research portion
'''
1. The average salary for a software engineer living in the Los Angeles area is $100,614

2. $100,614 is about 1% of $10,000,000

3. Probably no one
'''
