from mingus.containers import Composition
from generate_pattern import generate_pattern
from mingus.midi import MidiFileOut

def generate_composition(pattern, progression_type, nb_bars, key="C", rythm=60):
    newComposition = Composition()
    left_hand = generate_pattern(key, pattern, progression_type, nb_bars)
    newComposition.add_track(left_hand)
    MidiFileOut.write_Composition("myComposition.mid", newComposition, rythm, False)
    # truc pour la main droite
    

#generate_composition(((1, 8, 1, "none", '=', 2), (5, 8, 1, "none", '+', 2), (1, 8, 1.5, "none", '=', 2), (5, 8, 1.5, "none", '+', 2), (2, 8, 2, "diese", '=', 2), (3, 8, 2.5, "none", '+', 2), (1, 8, 3, "none", '=', 2), (5, 8, 3, "none", '+', 2), (1, 8, 3.5, "none", '=', 2), (5, 8, 3.5, "none", '+', 2), (2, 8, 4, "diese", '=', 2), (3, 8, 4.5, "none", '+', 2)), 12, 3, "D", 60)    
    
    
