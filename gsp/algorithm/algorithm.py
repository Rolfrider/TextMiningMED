import sys
import numpy as np
from collections import Counter
from model.sequence import Sequence


def search(min_sup: float, sequences: [Sequence]):
    min_sup_absolute = int(min_sup * len(sequences))
    k = 1
    while True:
        # Generate new candidates
        # Prune candidates
