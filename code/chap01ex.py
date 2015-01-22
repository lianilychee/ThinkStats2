"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

Exercise 1.2 Write code that reads the respondent file,
2002FemResp.dat.gz.
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def readFile(dct_file='2002FemResp.dct',
			 dat_file='2002FemResp.dat.gz'):
	""" Read NSFG pregnancy data.
	"""
	dct = thinkstats2.ReadStataDct(dct_file)
	df = dct.ReadFixedWidth(dat_file, compression='gzip')
	# CleanFemResp(df)
	return df


def checkPregnum(resp):
	# get pregnancy frame
	preg = nsfg.ReadFemPreg()

	# create map
	pregMap = nsfg.MakePregMap(preg)

	for index, pregnum in resp.pregnum.iteritems():
		caseid = resp.caseid[index]
		indices = pregMap[caseid]

		# check that pregnum from resp file = number of records in preg file
		if len(indices) != pregnum:
			print (caseid, len(indices), pregnum)
			return False

	return True


def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    resp = readFile()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(checkPregnum(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)