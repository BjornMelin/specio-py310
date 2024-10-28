###################
specio_py310's user API
###################

Spectra reader functions
========================

These functions represent specio_py310's main interface for the user. They provide a
common API to read spectra data for a large variety of formats. All read
functions accept keyword arguments, which are passed on to the format that does
the actual work.  To see what keyword arguments are supported by a specific
format, use the :func:`.help` function.

Functions for reading:

  * :func:`.specread` - read a file with spectra from the specified uri

For a larger degree of control, specio_py310 provides a function
:func:`.get_reader`. It returns an :class:`.Reader` object, which can be used
to read data and meta data in a more controlled manner.  This also allows
specific scientific formats to be exposed in a way that best suits that
file-format.

Functions
---------

.. autosummary::
   :toctree: generated/
   :template: function.rst

   specio_py310.help
   specio_py310.show_formats
   specio_py310.specread
   specio_py310.get_reader

Classes
-------

.. autosummary::
   :toctree: generated/
   :template: class.rst

   specio_py310.core.format.Reader

Core data structure
===================

:func:`specio_py310.specread` will return either a list of instances or an instance
from the class :class:`specio_py310.core.Spectrum`. This class is composed of three
attributes:

* a 1D ndarray of shape (n_wavelength,) or 2D ndarray of shape
  (n_spectra, n_wavelength) ``amplitudes`` containing the counts/amplitude for
  the different wavelengths;
* a 1D ndarray of shape (n_wavelength,) ``wavelength`` containing the
  wavelength for which the spectra have been acquired;
* a dictionary ``meta`` containing the metadata.

For more information, you can check the full API documentation above.

.. autosummary::
   :toctree: generated/
   :template: class.rst

   specio_py310.core.Spectrum

Command line interface
======================

``specio_py310`` provides a command line interface to make basic data manipulation.

Conversion to CSV
-----------------

Any format can be exported using the ``specio_py310`` command line::

  specio_py310 convert input_file.spc output_file.csv

``convert`` receive the input and output arguments. It is also possible to omit
the output argument and an automatic output file will be generated depending of
the input file name::

  specio_py310 convert input_file.spc

As with :func:`specio_py310.specread`, an input can get a name with a wildcard::

  specio_py310 convert "*.spc"

In addition, this is also possible to increase the tolerance to aggregate
several spectra in the same CSV as in :func:`specio_py310.specread`::

  specio_py310 convert "*.spc" --tolerance 1e-2

Example datasets
================

.. automodule:: specio_py310.datasets
    :no-members:
    :no-inherited-members:

.. currentmodule:: specio_py310

.. autosummary::
   :toctree: generated/
   :template: function.rst

   datasets.load_csv_path
   datasets.load_fsm_path
   datasets.load_mzml_path
   datasets.load_sp_path
   datasets.load_spc_path
 
