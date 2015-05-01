# -*- coding: utf-8 -*-
"""
Counting DNA Nucleotides
http://rosalind.info/problems/dna/

Transcribing DNA into RNA
http://rosalind.info/problems/revc/

Complementing a Strand of DNA
http://rosalind.info/problems/rna/
"""

############################
# DNA
# Counting DNA Nucleotides
DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'


def countN(seq, base):
    return seq.count(base)

print 'Counting DNA Nucleotides'
print countN(DNA, 'A'), countN(DNA, 'C'), countN(DNA, 'G'), countN(DNA, 'T')


############################
# RNA
# Transcribing DNA into RNA
DNA_STRING = 'GATGGAACTTGACTACGTAAATT'


def DnaToRna(seq):
    return seq.replace('T', 'U')

print 'Transcribing DNA into RNA'
print DnaToRna(DNA_STRING)


############################
# REVC
# Complementing a Strand of DNA
STRAND = 'AAAACCCGGT'


def reverseComplement(seq):
    dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    rev = ''
    for i in seq:
        rev += dict[i]
    return rev[::-1]

print 'Complementing a Strand of DNA'
print reverseComplement(STRAND)
