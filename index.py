#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* This is a Python port of https://github.com/utopiaio/Ethiopic-Calendar
*
* For more info have a look at: http://www.geez.org/Calendars/
* Java Code at https://github.com/geezorg/geezorg.github.io/blob/master/Calendars/EthiopicCalendar.java
* JavaScript Code at https://github.com/utopiaio/Ethiopic-Calendar
*/
"""
import calendar

JD_EPOCH_OFFSET_AMETE_ALEM = -285019    # ዓ/ዓ
JD_EPOCH_OFFSET_AMETE_MIHRET = 1723856  # ዓ/ም
JD_EPOCH_OFFSET_GREGORIAN = 1721426


def mod(i, j):
    return (i - (j * (i / j)))


def ethCopticToJDN(year, month, day, era):
    """
    Computes the Julian day number of the given Coptic or Ethiopic date.
    This method assumes that the JDN epoch offset has been set. This method
    is called by copticToGregorian and ethiopicToGregorian which will set
    the jdn offset context.

    :year: year in the Ethiopic calendar
    :month: month in the Ethiopic calendar
    :day: date in the Ethiopic calendar
    :era: [description]

    :returns: The Julian Day Number (JDN)
    """
    return (era + 365) + 365 * (year - 1) + (year / 4) + 30 * month + day - 31


def jdnToGregorian(jdn, JD_OFFSET=JD_EPOCH_OFFSET_GREGORIAN, leapYear=calendar.isleap):
    """
    Converts JDN to Gregorian

    :jdn:
    :JD_OFFSET:
    :leapYear:
    :returns:
    """
    nMonths = 12
    monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    r2000 = mod((jdn - JD_OFFSET), 730485)
    r400 = mod((jdn - JD_OFFSET), 146097)
    r100 = mod(r400, 36524)
    r4 = mod(r100, 1461)

    n = mod(r4, 365) + 365 * (r4 / 1460)
    s = (r4 / 1095)
    aprime = 400 * ((jdn - JD_OFFSET) / 146097) + 100 * (r400 / 36524) + 4 * (r100 / 1461) + (r4 / 365) - (r4 / 1460) - (r2000 / 730484)
    year = aprime + 1
    t = ((364 + s - n) / 306)
    month = t * ((n / 31) + 1) + (1 - t) * (((5 * (n - s) + 13) / 153) + 1)
    n += 1 - (r2000 / 730484)
    day = n

    if ((r100 == 0) and (n == 0) and (r400 != 0)):
        month = 12
        day = 31
    else:
        monthDays[2] = 29 if (leapYear(year)) else 28
        for i in range(1, nMonths+1):
            if n <= monthDays[i]:
                day = n
                break
            n -= monthDays[i]
    return (year, month, day)


def guessEra(jdn, JD_AM=JD_EPOCH_OFFSET_AMETE_MIHRET, JD_AA=JD_EPOCH_OFFSET_AMETE_ALEM):
    """
    Guesses ERA from JDN

    :jdn:
    :returns: {Number}
    """
    return JD_AM if jdn >= (JD_AM + 365) else JD_AA


def gregorianToJDN(year=1, month=1, day=1, JD_OFFSET=JD_EPOCH_OFFSET_GREGORIAN):
    """
    Given year, month and day of Gregorian returns JDN

    :year:
    :month:
    :day:
    :JD_OFFSET:
    :returns:
    """
    s = (year / 4) - ((year - 1) / 4) - (year / 100) + ((year - 1) / 100) + (year / 400) - ((year - 1) / 400)
    t = ((14 - month) / 12)
    n = 31 * t * (month - 1) + (1 - t) * (59 + s + 30 * (month - 3) + ((3 * month - 7) / 5)) + day - 1
    j = JD_OFFSET + 365 * (year - 1) + ((year - 1) / 4) - ((year - 1) / 100) + ((year - 1) / 400) + n
    return j

def jdnToEthiopic(jdn, era=JD_EPOCH_OFFSET_AMETE_MIHRET):
    """
    Given a JDN and an era returns the Ethiopic equivalent

    :jdn:
    :era:
    :returns: (year, month, day)
    """
    r = mod((jdn - era), 1461)
    n = mod(r, 365) + 365 * (r / 1460)
    year = 4 * ((jdn - era) / 1461) + (r / 365) - (r / 1460)
    month = (n / 30) + 1
    day = mod(n, 30) + 1
    return year, month, day


def ethiopicToGregorian(year=1, month=1, day=1, era=JD_EPOCH_OFFSET_AMETE_MIHRET):
    return jdnToGregorian(ethCopticToJDN(year, month, day, era))


def gregorianToEthiopic(year=1, month=1, day=1):
    jdn = gregorianToJDN(year, month, day)
    return jdnToEthiopic(jdn, guessEra(jdn))
