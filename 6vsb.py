import collections
import itertools
import os
import random
import urllib.request

import pyknon.genmidi
import pyknon.music

if __name__ == "__main__":
    with open("./data/rcsb_pdb_6VSB.fasta") as fp:
        sequence = fp.read()

    sequence = sequence.splitlines()[-1].strip()

    bases = {
        "A": 0,
        "R": 1,
        "N": 2,
        "D": 3,
        "B": 4,
        "C": 5,
        "Q": 6,
        "E": 7,
        "Z": 8,
        "G": 9,
        "H": 10,
        "I": 11,
        "L": 12,
        "K": 13,
        "M": 14,
        "F": 15,
        "P": 16,
        "S": 17,
        "T": 18,
        "W": 19,
        "Y": 20,
        "V": 21
    }

    notes = []

    for note in [bases[base] for base in sequence]:
        notes += [pyknon.music.Note(note)]

    midi = pyknon.genmidi.Midi()

    midi.seq_notes(pyknon.music.NoteSeq(notes))

    midi.write(os.path.join("data", "6vsb.midi"))
