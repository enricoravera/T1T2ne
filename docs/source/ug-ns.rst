.. _sec;ns:

The ``ns`` subcommand
*********************

This subcommand estimates the number of scans required for a given experiment, starting from an HSQC experiment.
There are two ways the estimate of SNR is done:

    A.  By direct estimation of the SNR from the 2D spectrum using :func:`klassez.anal.snr`.
    A.  By estimating the SNR from the envelope of the first ser of the hsqc or of the TRACT, and using the expected linewidh and the number of resonances to compute the expected intensity for a single peak.

In both cases the user needs to provide the path to an experiment to analyze through the parameters ``basedir`` and either ``hsqc`` or ``tract``. 
If for instance the dataset is in `/path/to/my/dataset/42`, these arguments should be passed as ``--basedir /path/to/my/dataset --hsqc 42``.
The expected reduction in intensity for the experiment to be setup with respect to this reference HSQC should be passed as a percentage value through the argument ``xred``.
The calculation is performed for each entry of the ``--xred`` argument list.
The first method is more accurate, but requires the user to have already acquired an HSQC spectrum of the sample, using the same parameters (type of sequence, number of transients) as those for relaxation.
This is used with:

    t1t2ne ns --basedir <basedir> --hsqc <HSQC experiment number> --xred 10 30 70 --snr2d

The second method is intrinsically less accurate, but the guess is still within a decent ballpark, and it can be used even before acquiring any 2D spectrum of the sample.
Taking as example a protein of 8.6 kDa (ubiquitin), the script is invoked by typing:
::

    t1t2ne ns --MW 8.6 --basedir <basedir> --hsqc <HSQC experiment number> --xred 10 30 70

The algorithm works as follows:

    1.  The HSQC spectrum is phased and integrated.
    1.  The number of signals under the integrated region are either counted on the basis of the MW, or provided by the user.
    1.  The SNR for each signal is then estimated.
    1.  The number of scans required to reach a SNR of 10 (the conventional quantitativity limit) at the longest delay (i.e. the worst case) is estimated.
    1.  The number of scans is rounded to the nearest multiple of 4 for the hetNOE experiment, and to the nearest multiple of 8 for the T\ :sub:`1`\  and T\ :sub:`2`\  experiments to respect phase cycling.


.. seealso::

   :class:`t1t2ne.scripts.t1t2ne_ns`
   :func:`klassez.anal.snr`


