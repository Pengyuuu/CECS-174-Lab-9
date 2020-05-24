def get_interstate_number():
    # ask for route number, validate it, return number
    number = -1
    while number < 0:
        number = input('Please enter a US Interstate Highway route number: ')
        if number[0:10] == 'Interstate':
            number = number[11:]
            number = int(number)
        elif number.find('-') == 1:
            number = number[2:]
            number = int(number)
        elif number.startswith('I') == True:
            number = number[1:]
            number = int(number)
        number = int(number)
    return number

def is_primary(number):
    # see if route number is primary or not
    x = len(str(number))
    if x == 3:
        return False
    else:
        return True
def compass_orientation(number):
    # see how the route is oriented
    number = int(number)
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
    number = str(number)
    x = number[0]
    x = int(x)
    y = x % 2
    even = 'radial highway'
    odd = 'spur highway'
    if y == 0:
        return even
    else:
        return odd
def parent_highway(number):
    # find parent highway from route number
    number = str(number)
    start = len(number) - 2
    result = number[start:len(number)]
    if number[start] == '0':
        result = result[1]
        return result
    else:
        return result
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