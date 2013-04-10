from mingus.core import intervals as intervals

def progression_to_int(progression):
    num_progression = []
    
    for prog in progression :
        roman = prog.upper()
        nums = ['X', 'V', 'I']
        ints = [10,  5,   1]
        places = []
  
        for i in range(len(roman)):
            c = roman[i]
            value = ints[nums.index(c)]
            # If the next place holds a larger number, this value is negative.
            try:
                nextvalue = ints[nums.index(roman[i +1])]
                if nextvalue > value:
                    value *= -1
            except IndexError:
                # there is no next place.
                pass
            places.append(value)
        sum_roman = 0
        for n in places: 
            sum_roman += n
        num_progression.append(sum_roman)
        
    return num_progression

def get_progression_key(note_int, key):
    if note_int == 1 :
        p_key = intervals.unison(key)
    if note_int == 4 :
        p_key = intervals.fourth(key, key)
    if note_int == 5 :
        p_key = intervals.fifth(key, key)
    return p_key