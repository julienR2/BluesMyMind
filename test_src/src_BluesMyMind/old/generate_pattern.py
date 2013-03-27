#!/Applications/python2.7

#Import the library

from midiutil.MidiFile import MIDIFile

def generate_mesure_pattern(pattern=[(1, 1, 0, 48), (3, 1, 1, 48), (5, 1, 2, 48), (7, 1, 3, 48)], gamme = 0) :


    # Create the MIDIFile Object with 1 track

    MyMIDI = MIDIFile(1)



    # Tracks are numbered from zero. Times are measured in beats.

    track = track  

    time = 0



    # Add track name and tempo.

    MyMIDI.addTrackName(track,time,"Sample Track")

    MyMIDI.addTempo(track,time,120)



    # Add a note. addNote expects the following information:

    track = track

    channel = 0

    #pitch = note generée 

    time = 0

    duration = 1

    volume = 100



    # Now add the note.

    MyMIDI.addNote(track,channel,pitch,time,duration,volume)
    print("lapin")


    # And write it to disk.

    binfile = open("output.mid", 'wb')

    MyMIDI.writeFile(binfile)

    binfile.close()


