def main():
    country = 0
    #create placings list
    placings = ['United States', 'Sweden', 'Switzerland', 'Canada', 'Great Britain', 'Norway', 'South Korea', 'Japan', 'Italy', 'Denmark']
    medals = ['Gold', 'Silver', 'Bronze']

    #loop it until they hit quit
    while country != 'Quit':

        #prompt user for country input
        country = input('Please enter a country or "Quit": ')

        #find index of correct country
        for i in range(len(placings)):
            if country == placings[i]:
                placing = i

        #give placement based on index
        if country == 'Quit':
            break
        elif placing <= 3 and placing > -1:
            print(country,'placed',placing + 1,medals[placing])
        elif placing >= 4 and placing < 10:
            print(country,'placed',int(placing) + 1)
        else:
            print(country,'did not compete') 
    
    #user has put in quit 
    print('Goodbye!')
main()

'''
Research Questions:
1a. Stone - A large, polished circular stone with an iron handle on top, used in the game of curling
b. House - The rings or circles toward which play is directed consisting of a 12-foot ring, 8-foot ring, 4-foot ring, and a button
c. Button - The circle at the center of the house
d. Sweeper - The players who sweeps the ice
e. Skip - The player who determines the strategy, and directs play for the team. The skip delivers the last pair 
of stones for his/her team in each end
2. Norway
3. Biathlon
'''