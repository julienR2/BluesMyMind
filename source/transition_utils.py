def get_nb_note_needed(last_bar, first_bar):
    nb_last = nb_note_bar(last_bar)
    nb_first = nb_note_bar(first_bar)
    dif = abs(nb_last - nb_first)
    
    if dif < 3 :
        return [nb_last, nb_first]

    else :
        if nb_last > nb_first :
            return [nb_last - (dif/2), nb_first + (dif/2)]
        else :
            return [nb_last + (dif/2), nb_first - (dif/2)]
    


def nb_note_bar(bar):
    number_notes = 0
    note_temp = 0
    for note in bar :
        if note_temp == 0:
            number_notes+=1
        else:
            if note[2]!=note_temp[2]:
                number_notes+=1
        note_temp = note
        
    return number_notes

def get_list_notes(last_bar, first_bar):
    return None