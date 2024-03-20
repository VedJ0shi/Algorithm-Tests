#C4-18

def is_moreVowels(s, instances={'vowels':0, 'consonants':0}):
    '''determines if str s has more vowels (aeiou) than consonants using dictionary'''

    if len(s) == 0: #base case
        if instances['vowels'] >  instances['consonants']:
            return True
        return False

    match s[-1].casefold():

        case 'a' |'e' | 'i' |  'o' | 'u':
            instances['vowels'] = instances.get('vowels', 0) + 1
        case _ :
            instances['consonants'] = instances.get('consonants', 0) + 1
        
    #print(vars())
    
    return is_moreVowels(s[:-1], instances)

    
