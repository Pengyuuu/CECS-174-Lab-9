def get_interstate_number():
    # ask for route number, validate it, return number
    number = int(input('Please enter a US Interstate Highway route number: '))
    while number < 0:
        number = int(input('Please enter a US Interstate Highway route number: '))
    return number

def is_primary(number):
    # see if route number is primary or not
    if number >= 100:
        return False
    else:
        return True
def compass_orientation(number):
    # see how the route is oriented
    x = number % 2
    even = 'east-west'
    odd = 'north-south'
    if x == 0:
        return even
    else:
        return odd

def is_arterial(number):
    # see if route is arterial or not
    x = number % 5
    if x == 0:
        return True
    else:
        return False
def auxiliary_type(number):
    # see if the route is auxiliary or not
    number = number // 100
    even = 'radial highway'
    odd = 'spur highway'
    if number % 2 == 0:
        return even
    else:
        return odd
def parent_highway(number):
    # find parent highway from route number
    x = number % 100
    return x
def main():
    # get route number and check if it is primary or not
    number = get_interstate_number()
    primary = is_primary(number)
    # if it is primary, find out it's orientation and arterial
    if primary == True:
        orientation = compass_orientation(number)
        arterial = is_arterial(number)
        if arterial == True:
            print('Interstate ',number,' is a long-distance arterial highway oriented ',orientation,'.',sep='')
        else:
            print('Interstate ',number,' is oriented ',orientation,'.',sep='')
    # otherwise, find it's auxiliary and parent
    else:
        auxiliary = auxiliary_type(number)
        parent = parent_highway(number)
        if auxiliary == 'spur highway':
            print('Interstate ',number,' is a ',auxiliary,' of Interstate ',parent,'.', sep='')
        else:
            print('Interstate ',number,' is a ',auxiliary,' of Interstate ',parent,'.',sep='')
    
main()

'''
Research Questions:
1. Dwight D. Eisenhower
2. Interstate 405
3. Bellingham, Washington, there is a interstate 405 in Washington
'''