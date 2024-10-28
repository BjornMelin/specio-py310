----------------------
specio_py310's developer API
----------------------

..
    We just import the whole of specio_py310.core
    The imageio.core docstring and __all__ are modified in
    at the init of documenation building to make this show
    all members and give a nice overview.

This page lists the developer documentation for specio_py310. Normal users
will generally not need this, except perhaps the :class:`.Format` class.
All these functions and classes are available in the ``specio_py310.core``
namespace.


.. currentmodule:: specio_py310.core

.. autosummary::
   :toctree: generated/

   Format
   FormatManager
   Request
   Dict
   Spectrum
   CannotReadSpectraError
