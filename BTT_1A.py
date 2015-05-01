# -*- coding: utf-8 -*-
"""
http://rosalind.info/problems/1a/
Frequent Words Problem

Find the most frequent k-mers in a string.
Given:  A DNA string Text and an integer k.
Return: All most frequent k-mers in Text (in any order).

Example:
ACGTTGCATGTCGCATGATGCATGAGAGCT
4

Output:
CATG GCAT

Usage: python BTT_1A.py 'ACGTTGCATGTCGCATGATGCATGAGAGCT' 4
"""
import sys
from collections import defaultdict

# Data input
seq = sys.argv[0]
k = sys.argv[1]

# Finding k-mers
kmers = defaultdict(int)


def FindKmer(seq, k):
    '''
    Returns a list the most frequent k-mer(s) in a given DNA sequence.

    Input:  DNA sequence (string), k-mer (integer)
    Output: List of k-mer DNA sequences (strings)
    '''
    seq = seq.upper()
    assert set(seq).issubset(set(['A', 'C', 'T', 'G', 'N'])), 'Invalid bases'
    for i in range(0, len(seq)-(k-1)):
        kmers[seq[i:i+k]] += 1
    return [key for key, val in kmers.iteritems()
            if val == max(kmers.values())]

if __name__ == '__main__':
    print FindKmer(seq, k)

# Testcase
# print FindKmer('ACGTTGCATGTCGCATGATGCATGAGAGCT' 4)
