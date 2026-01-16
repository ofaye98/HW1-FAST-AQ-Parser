# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)

import pytest

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    assert transcribe("ACTG") == "UGAC"
    assert transcribe("actg") == "UGAC"   # lowercase input should work
    assert transcribe("AcTg") == "UGAC"   # lower/uppercase input should work

    # check if user inputted an invalid nucleotide (ex. X)
    with pytest.raises(ValueError, match=r"Invalid nucleotide:\s*X"):
        transcribe("ACTX")

def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    assert reverse_transcribe("ACTG") == "CAGU"
    assert reverse_transcribe("actg") == "CAGU"   # lowercase input should work
    assert reverse_transcribe("AcTg") == "CAGU"   # lower/uppercase input should work

    # check if user inputted an invalid nucleotide (ex. X)
    with pytest.raises(ValueError, match=r"Invalid nucleotide:\s*X"):
        reverse_transcribe("ACTX")