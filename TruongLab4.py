#ask for price and years and validate
car_price = float(input('What is the original price of your automobile?: '))

while car_price < 1:
    car_price = float(input('What is the original price of your automobile?: '))

years = int(input('How many years have you had your car?: '))

while years < 1:
    years = int(input('How many years have you had your car?: '))

time = 1
#calculation loop
for i in range(years):
    value_lost = car_price * .18
    price = car_price - value_lost
    car_price = price
    print('Year',time,'value: $',format(car_price, ',.2f'), sep='')
    time += 1

'''
1. Half of $49311 is $24655.50 and with a loss of 18% of value each year (about
$8875.98), it would take about 3 and a half years to be half it's original price

'''
    
