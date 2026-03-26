.. _sec;solventpre:

The ``solventpre`` subcommand
*****************************

This subcommand generates the lists for running :math:`^1` H T\ :sub:`1`\  and T\ :sub:`2`\  solvent PRE experiments. T
It can be called providing only the field as:

::

    t1t2ne solventpre --Larmor 600

Alternatively, the user can provide the expected intrinsic T\ :sub:`1`\  of the system and/or the expected linewidth:

::

    t1t2ne solventpre --Larmor 600 --T1 1 --lw 10

The expected linewidth can also be estimated from the molecular weight of the system:

::

    t1t2ne solventpre --Larmor 600 --MW 8.6

By default, the software will suggest a list of 8 delays for T\ :sub:`1`\  and 2 points for T\ :sub:`2`\ , as described by Iwahara, Tang, and Clore in `10.1016/j.jmr.2006.10.003`_. The number of points can be changed with the ``--nT`` argument.
    
    .. _10.1016/j.jmr.2006.10.003: https://doi.org/10.1016/j.jmr.2006.10.003


**Important**: The delays are calculated under the assumption that the pulse sequence used for T\ :sub:`2`\  is the one found in figure 1 of `10.1016/j.jmr.2006.10.003`_.:
