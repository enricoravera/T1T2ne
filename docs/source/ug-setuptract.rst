.. _sec;setuptract:

The ``setuptract`` subcommand
*****************************

This subcommand generates the delay list for running a TRACT experiment on the spectrometer, providing the appropriate delay list based on the correlation time or molecular weight.
The general syntax for this command is the following:
::

    t1t2ne setuptract --MW <MW> --Larmor <Frequency in MHz>

The rationale is the same as for the ``makelists`` subcommand (see :ref:`sec;makelists`), where the correlation times of the system are either provided by the user or computed from the molecular weight, and the relaxation rates computed accordingly.
The the Larmor frequency of \ :sup:`1`\ H at the given field is needed unless the program is run on the spectrometer, in which case this information is not needed, as it is direcly taken from there.

The software will then generate a delay list for the TRACT experiment that covers a range of delays that is appropriate for the expected correlation time, and that maximizes the `Fisher Information criterium`_ for matching the decay rates of both :math:`\alpha` and :math:`\beta` components of the TROSY.

.. seealso::

   :class:`t1t2ne.scripts.t1t2ne_setuptract`


.. rubric:: Examples

If I have a 8.6 kDa protein (ubiquitin) and a 600 MHz spectrometer, the script should be invoked as:

-   *Case 1:* I know the Molecular Weight and I am at the spectrometer computer
    ::

        t1t2ne setuptract --MW 8.6 

-   *Case 2:* I know the correlation time and I am at the spectrometer computer
    ::

        t1t2ne setuptract --tauc 66.6

-   *Case 3:* I know the Molecular Weight and I am `not` at the spectrometer computer
    ::

        t1t2ne setuptract --MW 8.6 --Larmor 600

-   *Case 4:* I know the correlation time and I am `not` at the spectrometer computer
    ::

        t1t2ne setuptract --tauc 66.6 --Larmor 600

In any case, the software will generate a delay list for the TRACT experiment that covers a range of delays that is appropriate for the expected correlation time, and that maximizes the `Fisher Information criterium`_ for matching the decay rates of both :math:`\alpha` and :math:`\beta` components of the \ :sup:`1`\ H- :sup:`15`\ N doublet. 

The output looks like this:

.. code-block:: console

    $ t1t2ne setuptract --MW 6.2 --Larmor 600

    **************************************************
    *                                                *
    *                  T-one-T-tune                  *
    *                                                *
    *               setuptract module                *
    *                                                *
    **************************************************
    *                 Main Author:                   *
    *                                                *
    *                 Enrico Ravera                  *
    *                                                *
    *      Dipartimento di Chimica "Ugo Schiff"      *
    *             University of Florence             *
    *                                                *
    *                       &                        *
    *                                                *
    *          Consorzio Interuniversitario          *
    *    Risonanze Magnetiche di Metalloproteine     *
    *                                                *
    *                 Contributors:                  *
    *                Francesco Bruno                 *
    *                                                *
    *                Letizia Fiorucci                *
    **************************************************

    TopSpin does not appear to be installed on this workstation.
    Config file not found in the curdir folder of topspin for any of the users in the nmrsuperuser list.

    Calculating the optimal vdlist for the TRACT experiment...

    Provided parameters:
    Correlation time(s): [3.8861600000000006e-09, 1e-11] s
    Order parameter(s) S2: [0.9]

    Estimated relaxation rates:
    R1:  2.32 s^-1, R2: 5.98 s^-1, nOe: 0.75
    Ra:  1.56 s^-1
    Rb:  10.40 s^-1

    Suggested vdlist for TRACT experiment:
    --------------------------------------
    10.00u
    50.34u
    253.40u
    1.28m
    6.42m
    0.06144
    0.40955
    0.81909

    *****************************************************

    Analysis complete. Below are the references for the methods used in this software.
    We can not nor we want to force you to cite any of these papers, but we - and likewise (we believe) the authors of the original papers - appreciate if you do.
    - Cavanagh, J., Fairbrother, W. J., Palmer III, A. G., Rance, M., & Skelton, N. J. (2007). Protein NMR spectroscopy: principles and practice. Academic Press. DOI: 10.1016/B978-0-12-164491-8.X5000-3

    - Lee, D., Hilty, C., Wider, G., Wüthrich, K. (2006). J. Magn. Reson., 178, 72-76 DOI: 10.1016/j.jmr.2005.08.014

    - Fushman, D. (2012). Determining Protein Dynamics from 15N Relaxation Data by Using DYNAMICS. In: Shekhtman, A., Burz, D. (eds) Protein NMR Techniques. Methods in Molecular Biology, vol 831. Humana Press. DOI: 10.1007/978-1-61779-480-3_24

    - Salvi, N., Abyzov, A., Blackledge, M. (2017). Atomic resolution conformational dynamics of intrinsically disordered proteins from NMR spin relaxation. Progress in Nuclear Magnetic Resonance Spectroscopy, 102-103, 43-60. DOI: 10.1016/j.pnmrs.2017.06.001

    *****************************************************


The software accepts several command line options to customize the procedure:

-   Parameters related to the acquisition of the experiments:

    -   ``--nT``: the number of increments in the suggested vdlist. Default is 8. If more than one value is provided, the first one will be used and the others will be discarded.
    -   ``--randomize``: whether to randomize the order of the values in the lists. Default is False.
    -   ``--Larmor``: the Larmor frequency of the spectrometer, in MHz. It will be read from the configuration file of the spectrometer.
    -   ``--B0``: the magnetic field strength of the spectrometer, in Tesla. It will  be read from the configuration file of the spectrometer.

-   Parameters related to the estimation of the correlation times and order parameters:

    -   ``--S2``: the Lipari-Szabo order parameter S2 to use for the calculation of tau_c. In IDP mode, two values should be provide, else only one
    -   ``--MW``: the molecular weight of the protein in kDa, to be used for estimating the longest correlation time (tau_slow in the IDP model).
    -   ``--tau``: the correlation times to use for the estimation of the initial delays. In IDP mode, two values should be provided, else only one. If not set, they will be estimated from the MW. Otherwise, default T\ :sub:`1`\ and T\ :sub:`2`\  values will be used for the non-IDP model, and the three-tau model described in `Bolognesi et al.`_ for the IDP model.
    -   ``--idp``: whether the system under study is an intrinsically disordered protein (IDP). If set, the software will use the three-tau model described above. Default is False.

        -   If set, it will also select a longer delay in the cpmg for the T\ :sub:`2`\  experiment, optimized for the expected relaxation behavior of IDPs as described by `Bolognesi et al.`_.
        -   If set, it will also select a longer delay for the T\ :sub:`1`\  experiment, to avoid excessive heating, because cross-correlations are less important in IDPs.
        -   the ``--MW`` argument will be used to compute the slowest correlation time.
        -   ``--corr_window_idp``: the length of the correlation window for the IDP model, in residues. Default is 20.

    -   ``--T``: the temperature in Kelvin, to be used for estimating the taus from MW. Default is 298 K.

-   Parameters related to relaxation:

    -   ``--r``: the length of the 1H-15N bond in Angstroms. Default is 1.02 A.
    -   ``--Deltasigma``: the chemical shift anisotropy of the 15N nucleus in ppm. Default is -160 ppm.
    -   ``--theta``: the angle between the 1H-15N bond and the principal axis of the CSA tensor in degrees. Default is 17 degrees.
    -   ``--nucs``: the nuclei to use for the calculation of the relaxation rates. Default is 1H and 15N.


