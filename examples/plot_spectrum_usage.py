"""
===================================================
General presentation of the Spectrum data structure
===================================================

This example illustrates how to create and use the ``specio_py310.core.Spectrum``
data structure.

"""

# Authors: Guillaume Lemaitre <guillaume.lemaitre@inria.fr>
# License: BSD3

from __future__ import print_function

import numpy as np

from specio_py310 import specread
from specio_py310.core import Spectrum
from specio_py310.datasets import load_spc_path

print(__doc__)

###############################################################################
# The ``Spectrum`` class provide a data structure which embeds the following
# information:
#
# * a 1D ndarray of shape (n_wavelength,) or 2D ndarray of shape
#   (n_spectra, n_wavelength) ``amplitudes``;
# * a 1D ndarray of shape (n_wavelength,) ``wavelength``;
# * a dict ``meta``.
#
# Therefore, an instance can be built using those three variable. We give a
# simple example below to create an instance containing 10 spectra with 5
# wavelengths.

n_spectra, n_wavelength = 10, 5
amplitude = np.random.random((n_spectra, n_wavelength))
wavelength = np.arange(n_wavelength)
metadata = {'nature': 'toy example'}

spectra = Spectrum(amplitude, wavelength, metadata)
print('The spectrum created has the representation: \n{}'.format(spectra))

###############################################################################
# The ``Spectrum`` instances are returned when using `specio_py310.specread`. We give
# a quick example to illustrate this case.

spc_filename = load_spc_path()
print('Reading the file from: {}'.format(spc_filename))
spectra = specread(spc_filename)
print('The spectrum read has the representation: \n{}'.format(spectra))
