=================
Python-fontconfig
=================

Python bindings for ngslib_ library

Requirement
-----------

- numpy_ scientific computation
- pysam_ (>0.8.2) SAM/BAM file manipulation
- argparse_ (required if Python2.6 is used)

.. _numpy: http://www.numpy.org/
.. _pysam: http://pysam.readthedocs.org/en/latest/
.. _argparse: http://pymotw.com/2/argparse/




Tested on
~~~~~~~~

- ``Python 2.6.*`` (64-bit)
- ``Python 2.7.*`` (64-bit)
- ``CentOS 6.4``
- ``Fedora 17``
- ``RedHat 5.5``
- ``Ubuntu 12.04`` (``python-dev`` and ``libpng-dev`` are required)


Installation
------------

From PyPI::

  >>> pip install ngslib

  or

  >>> easy_install ngslib

From source::

  >>> easy_install --editable  --build-directory . ngslib
  >>> cd ngslib
  >>> python setup.py install


Major modules
-------------

- **IO**: Read various biological data
- **DB**: Build DB for genomic data for fast query.
- **Pipeline**: Pipelines built using wrappers of commonly used tools.
- **Bed**: Genomic coordinates data format.
- **BedList**: A list of Bed instances.
- **TwoBitFile**: python module for retrieve fasta sequence from 2bit file.
- **BigWigFile**: python module for retrieve Wiggle region from BigWig file.
- **mFile**: uniform interface for input types including regular file, sys.stdin/stdout and StringFile.


Usage
-----

>>> import ngslib
>>> for tbed in ngslib.IO.BioReader('test.bed','bed'):
        print tbed

>>> bwf = ngslib.DB('test.bw','bigwig')
>>> for wig in bwf.fetch('chr1',1000,2000):
        print wig
>>> depth = bwf.pileup('chr1',3000,4000)
>>> bwf.close()


License
-------

This program is released under ``GPLv3`` license, see ``LICENSE`` for more detail.
