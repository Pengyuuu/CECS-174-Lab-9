#asks for input
player_name = input("Please enter player's full name: ")

#asks for their plate appearance
plate_appearance = int(input('How many times has the player appeared on plate?: '))

at_bats = int(input('How many times has the player been at bat?: '))
walks = int(input('How many times has the player walked?: '))

singles = int(input('How many times has the player hit a single?: '))

doubles = int(input('How many times has the player hit a double?: '))

triples = int(input('How many times has the player hit a triple?: '))

home_runs = int(input('How many times has the player hit a home run?: '))

#calculate everything
total_hits = singles + doubles + triples + home_runs

bat_average = total_hits / at_bats

slug_percentage = (singles + (2 * doubles) + (3 * triples) + (4 * home_runs)) / at_bats

base_percentage = (total_hits + walks) / plate_appearance

ops = slug_percentage + base_percentage

#print everything
print()
print(player_name, 'had: ')
print(total_hits, 'hits')
print(format(bat_average, ',.3f'), 'AVG')
print(format(slug_percentage, ',.3f'), 'SLG')
print(format(ops, ',.3f'), 'OPS''\n')

#research portion
'''
Babe Ruth has the all time highest career OPS statistic
Mike Trout has the highest career OPS statistic among active players
'''
