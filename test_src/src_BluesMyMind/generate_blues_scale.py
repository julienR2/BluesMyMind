from mingus.core.mt_exceptions import NoteFormatError
import mingus.core.notes as notes
import mingus.core.intervals as intervals

def generate_blues_scale(key = "C"):
    """Returns an ordered list of the notes of the blues scale in this key. \
For example: if the key is set to 'C', this function will return \
`['C', 'D#', 'F', 'F#', 'G', 'A#']`. \
This function will raise an !NoteFormatError if the key isn't recognised"""
    
    if not (notes.is_valid_note(key)):
        raise NoteFormatError, "Unrecognised format for key '%s'" % key

    result = []
    
    fifth_index = notes.fifths.index(key[0])
    print("fifth_index"+str(fifth_index))

    """result.append(notes.fifths[(fifth_index - 1) % 7] + key[1:])
    print("result : "+str(result))
    for x in notes.fifths[fifth_index:]:
        print("je boucle dans 1")
        result.append(x  + key[1:])
        print("result"+str(result))

    for x in notes.fifths[:(fifth_index - 1)]:
        print("je boucle dans 2")
        result.append(x + key[1:] + "#")
        print("result"+str(result))"""
    
    result.append(intervals.unison(key))
    result.append(notes.diminish(intervals.third(key,key)))
    result.append(intervals.fourth(key,key))
    result.append(notes.diminish(intervals.fifth(key,key)))
    result.append(intervals.fifth(key,key))
    result.append(notes.diminish(intervals.seventh(key,key)))
    
    # Remove redundant #'s and b's from the result
    result = map(notes.remove_redundant_accidentals, result)
    tonic = result.index(notes.remove_redundant_accidentals(key))

    result = result[tonic:] + result[:tonic]

    return result

