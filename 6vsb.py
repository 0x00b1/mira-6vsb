import enum
import os
import random

import numpy
import pyknon.genmidi
import pyknon.music
import sklearn.preprocessing


AMINO_ACIDS = {
    "A": ( 0,  89.094,  1.8),
    "C": ( 1, 121.154,  2.5),
    "D": ( 2, 133.104, -3.5),
    "E": ( 3, 147.131, -3.5),
    "F": ( 4, 165.192,  2.8),
    "G": ( 5,  75.067, -0.4),
    "H": ( 6, 155.156, -3.2),
    "I": ( 7, 131.175,  4.5),
    "K": ( 8, 146.189, -3.9),
    "L": ( 9, 131.175,  3.8),
    "M": (10, 149.208,  1.9),
    "N": (11, 132.119, -3.5),
    "P": (12, 115.132, -1.6),
    "Q": (13, 146.146, -3.5),
    "R": (14, 174.203, -4.5),
    "S": (15, 105.093, -0.8),
    "T": (16, 119.119, -0.7),
    "V": (17, 117.148,  4.2),
    "W": (18, 204.228, -0.9),
    "Y": (19, 181.191, -1.3)
}

masses = numpy.array([x for _, x, _ in AMINO_ACIDS.values()])[:, numpy.newaxis]
scales = numpy.array([x for _, _, x in AMINO_ACIDS.values()])[:, numpy.newaxis]

masses = sklearn.preprocessing.normalize(masses, axis=0)
scales = sklearn.preprocessing.normalize(scales, axis=0)

scales = numpy.absolute(scales)
scales = sklearn.preprocessing.minmax_scale(scales, feature_range=(50, 100), axis=0)
scales = numpy.int16(scales)

masses = masses.ravel()
scales = scales.ravel()

features = []

for x, (y, z) in enumerate(zip(masses, scales)):
    features += [(x, y, z)]

if __name__ == "__main__":
    with open("./data/rcsb_pdb_6VSB.fasta") as fp:
        sequence = fp.read()

    sequence = sequence.splitlines()[-1].strip()

    notes = []

    records = [dict(zip(AMINO_ACIDS.keys(), features))[amino_acid] for amino_acid in sequence]

    for index, x, y in records:
        notes += [pyknon.music.Note(index, dur=x, volume=y)]

    midi = pyknon.genmidi.Midi()

    midi.seq_notes(pyknon.music.NoteSeq(notes))

    midi.write(os.path.join("data", "6vsb.midi"))
