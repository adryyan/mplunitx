mplunitx
========

.. image:: https://img.shields.io/badge/version-0.1.0-blue
   :target: https://img.shields.io/badge/version-0.1.0-blue
.. image:: https://img.shields.io/badge/License-MIT-blue
   :target: https://github.com/exp4-age/agepy/blob/main/LICENSE

*mplunitx* is a Python package heavily inspired by the :math:`\text{\LaTeX}`
package `siunitx`_ intended to be used complementary with *matplotlib*.

*matplotlib* supports some :math:`\text{\LaTeX}` in its text rendering,
but not the use of *siunitx*.
This package aims to provide a similar functionality to *siunitx* by
imitating the `\num`, `\unit` and `\qty` commands with python functions,
which return strings with :math:`\text{\LaTeX}` code that *matplotlib*
understands.

For the labels of the axes, the *mplunitx* package additionally provides
a function for typesetting the variable name and unit with either "/" in
between or "[]" around the unit.


Installation
------------


Usage
-----


.. _siunitx: https://ctan.org/pkg/siunitx?lang=en
