#!/usr/bin/env python

"""The ``inputfile`` module can be imported as such::

    from pyne.simplesim import inputfile

Below is the reference for this module.



This module employs the modules `reactordef` and `material` to generate
plaintext input files for a general code. Support is provided for MCNPX, and
support for Serpent is not complete but should be straightforward. The
extension to other codes may require more effort.

- Write out
- Read in a JSON file input def.
"""

import abc

class IInput(object):
    """Abstract base class for classes that take system and option definitions
    to create an input file for a certain code (e.g. MCNPX, Serpent, MCODE,
    etc.).

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, optionsdef):
        """

        Parameters
        ----------
        reactordef : pyne.ReactorDefinition

        """
        pass

    @abc.abstractmethod
    def _walk(self, region):
        return

    @abc.abstractmethod
    def _cell(self, cell):
        """Returns a cell card string."""
        return

    @abc.abstractmethod
    def _infinite_cylinder_surface(self, surface):
        """Returns an infinite cylinder surface card."""
        return


class MCNPInput(IInput):
    """Contains a write method for each type of surface.
    """

    def __init__(self, optionsdef):
        pass

    def _cell(self, cell):
        """Returns a cell card string given a Cell card."""
        return

    def _infinite_cylinder_surface(self, surface):
        """Returns an infinite cylinder surface card."""
        return


class SerpentInput(IInput):
    """Must find the cell used for a given material, and would need to create
    more than one material if necessary.

    """
    pass


class JSONInput(IInput):
    """Ideally we can exchange file formats through something like this
    intermediate."""
    pass