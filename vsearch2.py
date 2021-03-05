def search4letters(phrase:str, letters:str='aeiou') -> set:
    '''return a set of the 'letters' found in 'phrase'.'''
    return set(letters).intersection(set(phrase))

search4letters('hitch-hiker', 'aeiou')

search4letters('galaxy', 'xyz')

search4letters('life, the universe, and everything', 'o')

import random
random.randint(0,25)