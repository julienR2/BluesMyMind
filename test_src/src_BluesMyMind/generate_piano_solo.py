#!/Applications/python2.7

from mingus.core import progressions, intervals
from mingus.core import chords as ch
from mingus.containers import NoteContainer, Note
from mingus.midi import fluidsynth
import time, sys
from random import random, choice, randrange

print("lapin")
SF2 = "198_u20_Electric_Grand.sf2"

#progression = ['I', 'I', 'I', 'I', 'IV', 'IV', 'I', 'I', 'V', 'IV', 'I', 'V']
progression = ['I7', 'I7', 'I7', 'I7', 'IV7', 'IV7', 'I7', 'I7', 'V7', 'IV7', 'I7', 'V7']

key = "C"

swing = True
play_solo = True

bar_length = 1.75
song_end = 2

# Control beginning of solos and chords
solo_start = 0
solo_end = 2


# Channels
solo_channel = 13

random_solo_channel = False

if not fluidsynth.init(SF2):
        print "Couldn't load soundfont", SF2
        sys.exit(1)

chords = progressions.to_chords(progression, key)
loop = 1
while loop < song_end:
        i = 0 

        if random_solo_channel:
                solo_channel = choice(range(5,8) + [11])

        for chord in chords:
                c = NoteContainer(chords[i])
                l = Note(c[0].name)
                n = Note('C')
                l.octave_down()
                l.octave_down()

                print ch.determine(chords[i])[0]


                # Create random solo over chord
                beats = [ random() > 0.5 for x in range(8)]
                t = 0
                for beat in beats:

                        # Play random note
                        if beat and play_solo and loop > solo_start and loop < solo_end:
                                fluidsynth.stop_Note(n)
                                if t % 2 == 0:
                                        n = Note(choice(c).name)
                                        
                                elif random() > 0.5:
                                        if random() < 0.46:
                                                n = Note(intervals.second(choice(c).name, key))
                                        elif random() < 0.46:
                                                n = Note(intervals.seventh(choice(c).name, key))
                                        else:
                                                n = Note(choice(c).name)

                                        if t > 0 and t < len(beats) - 1:
                                                if beats[t-1] and not beats[t+1]:
                                                        n = Note(choice(c).name)
                                fluidsynth.play_Note(n, solo_channel, randrange(80, 110))
                                print n

                                
                        if swing:
                                if t % 2 == 0:
                                        time.sleep( (bar_length / (len(beats) * 3)) * 4)
                                else:
                                        time.sleep( (bar_length / (len(beats) * 3)) * 2)
                        else:
                                time.sleep( bar_length / len(beats))
                        t += 1

                fluidsynth.stop_Note(n, solo_channel)
                i += 1
        print "-" * 20
        loop += 1
