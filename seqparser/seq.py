# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    seq = seq.upper() # makes sure sequence is in uppercase letters
    try:
        transcribed = "".join(TRANSCRIPTION_MAPPING[nuc] for nuc in seq) # get the correct mapping and concat into one string
    except KeyError as e:
        raise ValueError(f"Invalid nucleotide: {e.args[0]}") # if nuc isn't in mapping dict, throw ValueError
    return transcribed

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    seq = seq.upper()
    try:
        transcribed = "".join(TRANSCRIPTION_MAPPING[nuc] for nuc in seq)
    except KeyError as e:
        raise ValueError(f"Invalid nucleotide: {e.args[0]}")

    rv_transcribed = transcribed[::-1]
    return rv_transcribed
