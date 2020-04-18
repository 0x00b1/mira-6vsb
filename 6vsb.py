import os

import pyknon.genmidi
import pyknon.music

AMINO_ACIDS = {
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

if __name__ == "__main__":
    with open("./data/rcsb_pdb_6VSB.fasta") as fp:
        sequence = fp.read()

    sequence = sequence.splitlines()[-1].strip()

    notes = []

    for note in [AMINO_ACIDS[amino_acid] for amino_acid in sequence]:
        notes += [pyknon.music.Note(note)]

    midi = pyknon.genmidi.Midi()

    midi.seq_notes(pyknon.music.NoteSeq(notes))

    midi.write(os.path.join("data", "6vsb.midi"))
