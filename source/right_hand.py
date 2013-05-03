from phrases import PHRASE_MIDDLE

def choose_phrases(key, mode, composition_length):
    #choose a list of phrases that will be used : one per 4-bar group
    if composition_length == 1 :
        nb_phrases = 3
        list_of_possible = choose_chord_1_phrase()
    
    elif composition_length == 2 :
        nb_phrases = 5
    
    
    list=("test", "test")
    return list

def choose_chord_1_phrase(mode):
    list = ()
    for phrase in PHRASE_MIDDLE :
        if phrase[0] == 1 and phrase[1]==mode:
            list+=phrase          
    return list

