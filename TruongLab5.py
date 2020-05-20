#get magnitudes
def get_magnitude(number):
    number = str(number)
    magnitude = float(input('Please enter the magnitude for earthquake ' \
                            + number + ': '))
    return magnitude

#compare magnitudes
def compare_magnitude(magnitude1, magnitude2):
    force = (10) ** ((1.5) * (max(magnitude1, magnitude2) - min(magnitude1, \
                                                                magnitude2)))
    return force

#loop function
def get_run_again():
    x = int(input('To restart, press 1: '))
    return x

#main function
def main():
    x = 1
    while x == 1:
        magnitude1 = get_magnitude(1)

        magnitude2 = get_magnitude(2)

        force = compare_magnitude(magnitude1, magnitude2)

        print('An earthquake of magnitude',max(magnitude1,magnitude2),'is' \
              ,format(force, ',.1f'),'times more powerful than an earthquake ' \
              'of magnitude',min(magnitude1,magnitude2),'.')

        x = get_run_again()

#call main
main()

'''
1. a. 2011 Tohoku earthquake, Japan: 9.1 magnitude
b. 1989 Loma Prieta earthquake, San Francisco: 6.9 magnitude
c. 2010 Haiti earthquake: 7 magnitude

2. The 2011 Tohoku earthquake is 1,412.5 times more powerful than the 2010 Haiti

3. Tohoku death toll: 15, 894
Haiti death toll: 230,000

'''
