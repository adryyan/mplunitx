Welcome to the mplunitx documentation
=====================================

|versionshield| |licenseshield| |docsshield| |pypi|

*mplunitx* is a Python package heavily inspired by the LaTeX
package `siunitx`_ intended to be used complementary with *matplotlib*.

*matplotlib* supports some LaTeX in its text rendering,
but not the use of *siunitx*. Using *siunitx* is possible with
``text.usetex=True`` in the *matplotlib* rc settings, but this needs a
local installation of LaTeX and keeping the fonts consistent is not trivial.
*mplunitx* aims to provide a similar functionality to *siunitx* by
imitating the ``\num``, ``\unit`` and ``\qty`` commands with python functions,
which return strings with LaTeX code that *matplotlib* understands.

For the labels of the axes, the *mplunitx* package additionally provides
a function for typesetting the variable name and unit with either ``"/"`` in
between or ``"[]"`` around the unit.

.. toctree::
   :maxdepth: 1
   :hidden:

   installation
   reference
   tutorials


.. _siunitx: https://ctan.org/pkg/siunitx?lang=en