#!/usr/bin/python
#Last-modified: 09 Apr 2015 01:50:54 PM

#         Module/Scripts Description
# 
# Copyright (c) 2008 Yunfei Wang <yfwang0405@gmail.com>
# 
# This code is free software; you can redistribute it and/or modify it
# under the terms of the BSD License (see the file COPYING included with
# the distribution).
# 
# @status:  experimental
# @version: 1.1.0
# @author:  Yunfei Wang
# @contact: yfwang0405@gmail.com

# ------------------------------------
# python modules
# ------------------------------------

import os,sys
from setuptools import setup, find_packages, Extension

# ------------------------------------
# constants
# ------------------------------------

# ------------------------------------
# Misc functions
# ------------------------------------

# ------------------------------------
# Classes
# ------------------------------------

# ------------------------------------
# Main
# ------------------------------------

if __name__ == '__main__':
    if float(sys.version[:3])<2.6 or float(sys.version[:3])>=2.8:
        sys.stderr.write("CRITICAL: Python version must be 2.6 or 2.7!\n")
        sys.exit(1)

    # includepy = "%s/include/python%s" % (sys.prefix, sys.version[:3])
    with open("README.rst",'r') as fh:
        long_description = fh.read()
    # ngslib version
    with open('VERSION','r') as fh:
        PROG, VERSION = fh.read().split()

    # Compile Kent lib
    if 'clean' in sys.argv:
        print >>sys.stderr, "Clean KentLib ..."
        os.system('cd external/KentLib && make clean && cd ../..')
        print >>sys.stderr, "Clean dist and egg info ..."
        os.system('if [ -d dist ]; then rm -rf dist; fi')
        os.system('if [ -f ngslib.egg-info ]; then rm ngslib.egg-info; fi')
        os.system('if [ -d ngslib.egg-info ]; then rm -rf ngslib.egg-info; fi')
    else:
        print >>sys.stderr, "Compile KentLib ..."
        os.system('cd external/KentLib && make && cd ../..')
    
    # install requirement
    install_requires = [ ["numpy >= 1.4.1"],
                         ["pysam >= 0.8.2"]]
    # Python 2.6 requires argparse
    if float(sys.version[:3]) == 2.6:
        install_requires.append(["argparse >= 1.2.1"])

    setup(name=PROG,
          version=VERSION,
          author='Yunfei Wang',
          author_email='yfwang0405@gmail.com',
          url='http://tsznxx.appspot.com',
          license="GNU General Public License (GPL)",
          keywords = "Python Sequencing Bed BigWig TwoBit",
          description = ("Python Modules for Next-Generation Sequencing Data Analysis."),
          long_description = long_description,
          package_dir={'ngslib':'src'},
          packages = ['ngslib'],
          scripts=['bin/wSamToWig.py',
                   'bin/wBedToWig.py',    
                   'bin/wXLSToTXT.py',
                   'scripts/wBedExtend.py',
                   'scripts/wBedToFasta.py',
                   'bin/wSam2Bed.py',
                   'bin/wWigPlot.py',
                   'scripts/wGetTSS.py',
                   'scripts/wlncRNA.py',
                   'scripts/wGTFToTab.py',
                   'scripts/wTabToBed.py',
                   'scripts/wFormatFasta.py',
                   'scripts/wGCContent.py',
                   'scripts/wGetSeqByCoordinates.py',
                   'scripts/wGetSeqByName.py',
                   'scripts/wRandomBed.py',
                   'scripts/wFindNearestTwoAnnotation.py',
                   'scripts/wFindNearestAnnotation.py',
                   'scripts/wBedAnnotation.py',
                   'scripts/wBedGetWig.py',
                   'scripts/wGetIntron.py',
                   'scripts/wGetExon.py',
                   'scripts/wMergeSort.py'],
          ext_modules=[Extension('wWigIO',['external/KentLib/wWigIO/wWigIO.c'],extra_link_args=['-DMACHTYPE_x86_64','-lz','-lm','external/KentLib/lib/jkweb.a'],extra_compile_args='-w -shared -fPIC -p -Iexternal/KentLib/inc'.split(' ')),
                       Extension('wTwoBitIO',['external/KentLib/wTwoBitIO/wTwoBitIO.c'],extra_link_args=['-DMACHTYPE_x86_64','-lz','-lm','external/KentLib/lib/jkweb.a'],extra_compile_args='-w -shared -fPIC -p -Iexternal/KentLib/inc'.split(' '))],
          classifiers=['Environment :: Console',
                       'Development Status :: 3 - Alpha',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: GNU General Public License (GPL)',
                       'License :: Free for non-commercial use',
                       'Operating System :: Unix',
                       'Programming Language :: Python :: 2.7',
                       'Topic :: Scientific/Engineering :: Bio-Informatics'],
          install_requires=install_requires)

