#!/usr/bin/env python
# -*- coding: utf-8 -*-

from index import ethiopicToGregorian, gregorianToEthiopic, JD_EPOCH_OFFSET_AMETE_ALEM

print "Started testing"

assert ethiopicToGregorian(1855, 2, 20) == (1862, 10, 29), '1862-10-29'
assert ethiopicToGregorian(1857, 10, 29) == (1865, 7, 5), '1865-7-5'
assert ethiopicToGregorian(1858, 5, 22) == (1866, 1, 29), '1858-5-22'
assert ethiopicToGregorian(1858, 8, 10) == (1866, 4, 17), '1866-4-17'
assert ethiopicToGregorian(1859, 4, 28) == (1867, 1, 5), '1867-1-5'
assert ethiopicToGregorian(1860, 5, 5) == (1868, 1, 13), '1868-1-13'

assert ethiopicToGregorian(5492, 5, 7, JD_EPOCH_OFFSET_AMETE_ALEM) == (0, 1, 1), '0-1-1'
assert ethiopicToGregorian(5493, 5, 8, JD_EPOCH_OFFSET_AMETE_ALEM) == (1, 1, 1), '1-1-1'
assert ethiopicToGregorian(5499, 13, 6, JD_EPOCH_OFFSET_AMETE_ALEM) == (7, 8, 27), '7-8-27'

assert ethiopicToGregorian(5500, 1, 1, JD_EPOCH_OFFSET_AMETE_ALEM) == (7, 8, 28), '7-8-28'
assert ethiopicToGregorian(5500, 1, 2, JD_EPOCH_OFFSET_AMETE_ALEM) == (7, 8, 29), '1-1-1'
assert ethiopicToGregorian(1, 1, 1) == (8, 8, 27), '8-8-27'
assert ethiopicToGregorian(2, 1, 1) == (9, 8, 27), '9-8-27'
assert ethiopicToGregorian(3, 1, 1) == (10, 8, 27), '10-8-27'
assert ethiopicToGregorian(4, 1, 1) == (11, 8, 28), '11-8-28'

assert ethiopicToGregorian(5500, 13, 5, JD_EPOCH_OFFSET_AMETE_ALEM) == (8, 8, 26), '8-8-26'
assert ethiopicToGregorian(1, 13, 5) == (9, 8, 26), '9-8-26'
assert ethiopicToGregorian(2, 13, 5) == (10, 8, 26), '10-8-26'
assert ethiopicToGregorian(3, 13, 5) == (11, 8, 26), '11-8-26'
assert ethiopicToGregorian(3, 13, 6) == (11, 8, 27), '11-8-27'
assert ethiopicToGregorian(4, 13, 5) == (12, 8, 26), '12-8-26'

assert ethiopicToGregorian(1575, 2, 6) == (1582, 10, 13), '1582-10-13'
assert ethiopicToGregorian(1575, 2, 7) == (1582, 10, 14), '1582-10-14'

assert ethiopicToGregorian(1575, 2, 8) == (1582, 10, 15), '1582-10-15'
assert ethiopicToGregorian(1575, 2, 9) == (1582, 10, 16), '1582-10-16'

assert ethiopicToGregorian(1892, 4, 23) == (1900, 1, 1), '1900-1-1'
assert ethiopicToGregorian(1997, 4, 23) == (2005, 1, 1), '2005-1-1'
assert ethiopicToGregorian(2000, 13, 5) == (2008, 9, 10), '2008-9-10'

assert ethiopicToGregorian(1893, 4, 22) == (1900, 12, 31), '1900-12-31'
assert ethiopicToGregorian(1985, 4, 22) == (1992, 12, 31), '1992-12-31'
assert ethiopicToGregorian(1989, 4, 22) == (1996, 12, 31), '1996-12-31'
assert ethiopicToGregorian(1993, 4, 22) == (2000, 12, 31), '2000-12-31'
assert ethiopicToGregorian(1997, 4, 22) == (2004, 12, 31), '2004-12-31'
assert ethiopicToGregorian(2001, 4, 22) == (2008, 12, 31), '2008-12-31'
assert ethiopicToGregorian(2993, 4, 14) == (3000, 12, 31), '3000-12-31'
assert ethiopicToGregorian(3993, 4, 7) == (4000, 12, 31), '4000-12-31'
assert ethiopicToGregorian(5993, 3, 22) == (6000, 12, 31), '6000-12-31'




assert gregorianToEthiopic(1862, 10, 29) == (1855, 2, 20), '1855-2-20'
assert gregorianToEthiopic(1865, 7, 5) == (1857, 10, 29), '1857-10-29'
assert gregorianToEthiopic(1866, 1, 29) == (1858, 5, 22), '1858-5-22'
assert gregorianToEthiopic(1866, 4, 17) == (1858, 8, 10), '1858-8-10'
assert gregorianToEthiopic(1867, 1, 5) == (1859, 4, 28), '1859-4-28'
assert gregorianToEthiopic(1868, 1, 13) == (1860, 5, 5), '1860-5-5'

assert gregorianToEthiopic(0, 1, 1) == (5492, 5, 7), '5492-5-7'
assert gregorianToEthiopic(1, 1, 1) == (5493, 5, 8), '5493-5-8'
assert gregorianToEthiopic(7, 8, 27) == (5499, 13, 6), '5499-13-6'

assert gregorianToEthiopic(7, 8, 28) == (5500, 1, 1), '5500-1-1'
assert gregorianToEthiopic(7, 8, 29) == (5500, 1, 2), '5500-1-2'
assert gregorianToEthiopic(8, 8, 27) == (1, 1, 1), '1-1-1'
assert gregorianToEthiopic(9, 8, 27) == (2, 1, 1), '2-1-1'
assert gregorianToEthiopic(10, 8, 27) == (3, 1, 1), '3-1-1'
assert gregorianToEthiopic(11, 8, 28) == (4, 1, 1), '4-1-1'

assert gregorianToEthiopic(8, 8, 26) == (5500, 13, 5), '5500-13-5'
assert gregorianToEthiopic(9, 8, 26) == (1, 13, 5), '1-13-5'
assert gregorianToEthiopic(10, 8, 26) == (2, 13, 5), '2-13-5'
assert gregorianToEthiopic(11, 8, 26) == (3, 13, 5), '3-13-5'
assert gregorianToEthiopic(11, 8, 27) == (3, 13, 6), '3-13-6'
assert gregorianToEthiopic(12, 8, 26) == (4, 13, 5), '4-13-5'

assert gregorianToEthiopic(1582, 10, 13) == (1575, 2, 6), '1575-2-6'
assert gregorianToEthiopic(1582, 10, 14) == (1575, 2, 7), '1575-2-7'

assert gregorianToEthiopic(1582, 10, 15) == (1575, 2, 8), '1575-2-8'
assert gregorianToEthiopic(1582, 10, 16) == (1575, 2, 9), '1575-2-9'

assert gregorianToEthiopic(1900, 1, 1) == (1892, 4, 23), '1892-4-23'
assert gregorianToEthiopic(2005, 1, 1) == (1997, 4, 23), '1997-4-23'
assert gregorianToEthiopic(2008, 9, 10) == (2000, 13, 5), '2000-13-5'

assert gregorianToEthiopic(1900, 12, 31) == (1893, 4, 22), '1893-4-22'
assert gregorianToEthiopic(1992, 12, 31) == (1985, 4, 22), '1985-4-22'
assert gregorianToEthiopic(1996, 12, 31) == (1989, 4, 22), '1989-4-22'
assert gregorianToEthiopic(2000, 12, 31) == (1993, 4, 22), '1993-4-22'
assert gregorianToEthiopic(2004, 12, 31) == (1997, 4, 22), '1997-4-22'
assert gregorianToEthiopic(2008, 12, 31) == (2001, 4, 22), '2001-4-22'
assert gregorianToEthiopic(3000, 12, 31) == (2993, 4, 14), '2993-4-22'
assert gregorianToEthiopic(4000, 12, 31) == (3993, 4, 7), '3993-4-7'
assert gregorianToEthiopic(6000, 12, 31) == (5993, 3, 22), '5993-3-22'

print "Great success"
