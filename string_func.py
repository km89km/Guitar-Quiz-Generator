# function that will return a dictionary of the frets and their musical notes for
# the desired string based on it's open musical value; i.e. the tuned note of the string without
# any fretting applied; 6th = 'E', 5th = 'A' etc.
def string_notes(string):
    # list of the musical notes in order.
    notes = ['E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B',
             'C', 'C#/Db', 'D', 'D#/Eb']
    # re-arrange the notes so that the open string note is first.
    new_notes = notes[notes.index(string.upper()):] + notes[:notes.index(string.upper())]
    # create a dictionary by zipping together the fret numbers with their corresponding musical value.
    return dict(zip(range(12), new_notes))
