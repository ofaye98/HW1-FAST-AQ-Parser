# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest
from pathlib import Path # added this to access test .fa/q files

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2  

def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    project_root = Path(__file__).resolve().parents[1] # get previous directory from current (project root dir)
    data_dir = project_root/"data"
    tests_dir = Path(__file__).resolve().parent # get current directory (tests)

    # checking test fasta file in data folder
    testfasta_file_path = data_dir/"test.fa"
    assert testfasta_file_path.exists(), f"Expected {testfasta_file_path} to exist." # pass if file exists
    testfasta_records = list(FastaParser(str(testfasta_file_path))) 

    # checking FASTA invariants
    assert len(testfasta_records) > 0 # at least one fasta was loaded
    assert testfasta_records[0][0] is not None # header exists
    assert testfasta_records[0][1] is not None # sequence exists
    assert testfasta_records[0][1] != "" # sequence not empty

    # checking bad fasta file
    bad_fasta_file_path =  tests_dir/"bad.fa"
    assert bad_fasta_file_path.exists(), f"Expected {bad_fasta_file_path} to exist." 
    # pass if a ValueError is raised when loading a bad fasta file
    with pytest.raises(ValueError): 
        list(FastaParser(str(bad_fasta_file_path)))

    # checking blank fasta file
    blank_fasta_file_path =  tests_dir/"blank.fa"
    assert blank_fasta_file_path.exists(), f"Expected {blank_fasta_file_path} to exist." 
    # pass if a ValueError is raised when loading a blank fasta file
    blankfasta_records = list(FastaParser(str(blank_fasta_file_path)))
    with pytest.raises(ValueError, match=r"had 0 lines"): # must match this regex pattern, checks for correct failure reason
        list(FastaParser(str(blank_fasta_file_path)))

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    project_root = Path(__file__).resolve().parents[1]  
    data_dir = project_root/"data"

    testfasta_file_path = data_dir/"test.fa"
    testfastq_file_path = data_dir/"test.fq"

    # pass if files exist
    assert testfasta_file_path.exists(), f"Expected {testfasta_file_path} to exist."
    assert testfastq_file_path.exists(), f"Expected {testfastq_file_path} to exist."

    # FASTA should yield a real header (not None)
    fasta_records = list(FastaParser(str(testfasta_file_path)))
    assert fasta_records[0][0] is not None

    # FASTQ read by FastaParser: first "header" will be None (since lines start with '@', not '>')
    fastq_records = list(FastaParser(str(testfastq_file_path)))
    assert fastq_records[0][0] is None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    project_root = Path(__file__).resolve().parents[1]  
    data_dir = project_root/"data"

    testfastq_file_path = data_dir/"test.fq"
    assert testfastq_file_path.exists(), f"Expected {testfastq_file_path} to exist." # pass if file exists
    testfastq_records = list(FastqParser(str(testfastq_file_path))) 

    # checking FASTQ invariants
    assert len(testfastq_records) > 0 # at least one fastq was loaded
    assert testfastq_records[0][0] is not None # header exists
    assert testfastq_records[0][1] is not None # sequence exists
    assert testfastq_records[0][1] != "" # sequence not empty

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    project_root = Path(__file__).resolve().parents[1]  
    data_dir = project_root/"data"

    testfasta_file_path = data_dir/"test.fa"
    testfastq_file_path = data_dir/"test.fq"

    assert testfasta_file_path.exists(), f"Expected {testfasta_file_path} to exist."
    assert testfastq_file_path.exists(), f"Expected {testfastq_file_path} to exist."

    # FASTQ should yield a real header (not None)
    fastq_records = list(FastqParser(str(testfastq_file_path)))
    assert fastq_records[0][0] is not None

    # FASTA read by FastaParser: first "header" will be None
    fasta_records = list(FastqParser(str(testfasta_file_path)))
    assert fasta_records[0][0] is None