#!/usr/bin/env python
# -*- coding: utf-8 -*-

from index import (JD_EPOCH_OFFSET_AMETE_ALEM, ethiopicToGregorian,
                   gregorianToEthiopic)

print "Started testing"

ethiopic_to_gregorian_pairs = [
    [(1855, 2, 20), (1862, 10, 29)],
    [(1857, 10, 29), (1865, 7, 5)],
    [(1858, 5, 22), (1866, 1, 29)],
    [(1858, 8, 10), (1866, 4, 17)],
    [(1859, 4, 28), (1867, 1, 5)],
    [(1860, 5, 5), (1868, 1, 13)],
    [(5492, 5, 7, JD_EPOCH_OFFSET_AMETE_ALEM), (0, 1, 1)],
    [(5493, 5, 8, JD_EPOCH_OFFSET_AMETE_ALEM), (1, 1, 1)],
    [(5499, 13, 6, JD_EPOCH_OFFSET_AMETE_ALEM), (7, 8, 27)],
    [(5500, 1, 1, JD_EPOCH_OFFSET_AMETE_ALEM), (7, 8, 28)],
    [(5500, 1, 2, JD_EPOCH_OFFSET_AMETE_ALEM), (7, 8, 29)],
    [(1, 1, 1), (8, 8, 27)],
    [(2, 1, 1), (9, 8, 27)],
    [(3, 1, 1), (10, 8, 27)],
    [(4, 1, 1), (11, 8, 28)],
    [(5500, 13, 5, JD_EPOCH_OFFSET_AMETE_ALEM), (8, 8, 26)],
    [(1, 13, 5), (9, 8, 26)],
    [(2, 13, 5), (10, 8, 26)],
    [(3, 13, 5), (11, 8, 26)],
    [(3, 13, 6), (11, 8, 27)],
    [(4, 13, 5), (12, 8, 26)],
    [(1575, 2, 6), (1582, 10, 13)],
    [(1575, 2, 7), (1582, 10, 14)],
    [(1575, 2, 8), (1582, 10, 15)],
    [(1575, 2, 9), (1582, 10, 16)],
    [(1892, 4, 23), (1900, 1, 1)],
    [(1997, 4, 23), (2005, 1, 1)],
    [(2000, 13, 5), (2008, 9, 10)],
    [(1893, 4, 22), (1900, 12, 31)],
    [(1985, 4, 22), (1992, 12, 31)],
    [(1989, 4, 22), (1996, 12, 31)],
    [(1993, 4, 22), (2000, 12, 31)],
    [(1997, 4, 22), (2004, 12, 31)],
    [(2001, 4, 22), (2008, 12, 31)],
    [(2993, 4, 14), (3000, 12, 31)],
    [(3993, 4, 7), (4000, 12, 31)],
    [(5993, 3, 22), (6000, 12, 31)]
]

for ethiopic, gregorian in ethiopic_to_gregorian_pairs:
    assert ethiopicToGregorian(*ethiopic) == gregorian, gregorian


gregorian_to_ethiopic_pairs = [
    [(1862, 10, 29), (1855, 2, 20)],
    [(1865, 7, 5), (1857, 10, 29)],
    [(1866, 1, 29), (1858, 5, 22)],
    [(1866, 4, 17), (1858, 8, 10)],
    [(1867, 1, 5), (1859, 4, 28)],
    [(1868, 1, 13), (1860, 5, 5)],
    [(0, 1, 1), (5492, 5, 7)],
    [(1, 1, 1), (5493, 5, 8)],
    [(7, 8, 27), (5499, 13, 6)],
    [(7, 8, 28), (5500, 1, 1)],
    [(7, 8, 29), (5500, 1, 2)],
    [(8, 8, 27), (1, 1, 1)],
    [(9, 8, 27), (2, 1, 1)],
    [(10, 8, 27), (3, 1, 1)],
    [(11, 8, 28), (4, 1, 1)],
    [(8, 8, 26), (5500, 13, 5)],
    [(9, 8, 26), (1, 13, 5)],
    [(10, 8, 26), (2, 13, 5)],
    [(11, 8, 26), (3, 13, 5)],
    [(11, 8, 27), (3, 13, 6)],
    [(12, 8, 26), (4, 13, 5)],
    [(1582, 10, 13), (1575, 2, 6)],
    [(1582, 10, 14), (1575, 2, 7)],
    [(1582, 10, 15), (1575, 2, 8)],
    [(1582, 10, 16), (1575, 2, 9)],
    [(1900, 1, 1), (1892, 4, 23)],
    [(2005, 1, 1), (1997, 4, 23)],
    [(2008, 9, 10), (2000, 13, 5)],
    [(1900, 12, 31), (1893, 4, 22)],
    [(1992, 12, 31), (1985, 4, 22)],
    [(1996, 12, 31), (1989, 4, 22)],
    [(2000, 12, 31), (1993, 4, 22)],
    [(2004, 12, 31), (1997, 4, 22)],
    [(2008, 12, 31), (2001, 4, 22)],
    [(3000, 12, 31), (2993, 4, 14)],
    [(4000, 12, 31), (3993, 4, 7)],
    [(6000, 12, 31), (5993, 3, 22)],
]

for gregorian, ethiopic in gregorian_to_ethiopic_pairs:
    assert gregorianToEthiopic(*gregorian) == ethiopic, ethiopic

print "Great success"
