def get_word():
    #prompt user for word and return it
    word = input('Please enter a word: ')
    return word

def is_vowel(letter):
    #letter is a vowel return True, if not, return False
    c = letter
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or \
       c == 'u':
        return True
    else:
        return False
    

def calculate_measure(word):
    #calculate measure by checking when it goes from a vowel to a consonant
    counter = 0
    c = word[0]
    c = is_vowel(c)
    for i in range(1, len(word)):
        d = word[i]
        check = is_vowel(d)
        if check == False:
            if c == True:
                counter += 1
        c = check

    return counter
    
def main():
    word = get_word()
    counting = calculate_measure(word)
    print(word + ' has a measure of ',counting,'.', sep='' )
            
main()


