.. _sec;makelists:

The ``makelists`` subcommand
****************************

The scope of this subcommand is generally the same as the :ref:`sec;interactive`, i.e.: it generates the lists for running :sup:`15`\ N T\ :sub:`1`\  and T\ :sub:`2`\  relaxation experiments given the correlation times or the molecular weight.
At variance with the :ref:`sec;interactive`, however, it does not provide an interactive procedure to optimize the delays. For this reason, it is recommended to be used after the :ref:`sec;tract` experiment, to generate the lists for the final acquisition of the experiments with the optimized delays (see below).
As for the :ref:`sec;interactive`, this subcommand uses the name scheme of the two pulse sequences for T\ :sub:`1`\  and T\ :sub:`2`\  measurements provided with this package (`hsqct1etf3gptcwg1d.rav` and `hsqct2etf3gptcwg1d.rav`).

It is called as:

::
    
    t1t2ne makelists --MW 8.6 --Larmor 600


Which will generate the following output:

.. code-block:: console

    $ t1t2ne makelists --MW 8.6 --Larmor 600

    **************************************************
    *                                                *
    *                  T-one-T-tune                  *
    *                                                *
    *                makelists module                *
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

    No value provided for the xred parameter. Defaulting to [10, 30].
    TopSpin does not appear to be installed on a spectrometer workstation.
    Config file not found in the curdir folder of topspin for any of the users in the nmrsuperuser list.


    Estimated values for heteronuclear relaxation:

    expected T1 = 0.507 s
    expected T2 = 0.132 s
    expected hetnOe = 0.784
    Set the recovery delay for the hetnOe experiment in the range 2.026 - 3.039.

    Creating vdlist with 8 points and vclist with 8 points...


    The longest delay for the T1 experiment for a residual signal of 10% should be 1.17 s.

    vdlist for T1 experiment:
    -------------------------
    20.00u
    0.17000
    0.33000
    0.50000
    0.67000
    0.83000
    1.00000
    1.17000
    Enter the d21 value in microseconds (default 450): 
    Enter the p30 value in microseconds (default 160): 
    With the chosen d21 and p30 values, the maximum CPMG block allowed by the duty cycle is 0.25 s.
    Warning: the second CPMG point in logscale would be a repetition of the first, switching to "large" sequence
    The longest CPMG block for T2 for a residual signal of 30% should be 0.16 s, with 18 loops.
    Check if this is too long for your equipment before running the experiment

    vclist for T2 experiment:
    -------------------------
    0
    2
    5
    7
    10
    12
    15
    18



    *****************************************************

    Analysis complete. Below are the references for the methods used in this software.
    We can not nor we want to force you to cite any of these papers, but we - and likewise (we believe) the authors of the original papers - appreciate if you do.
    - Cavanagh, J., Fairbrother, W. J., Palmer III, A. G., Rance, M., & Skelton, N. J. (2007). Protein NMR spectroscopy: principles and practice. Academic Press. DOI: 10.1016/B978-0-12-164491-8.X5000-3

    - Fushman, D. (2012). Determining Protein Dynamics from 15N Relaxation Data by Using DYNAMICS. In: Shekhtman, A., Burz, D. (eds) Protein NMR Techniques. Methods in Molecular Biology, vol 831. Humana Press. DOI: 10.1007/978-1-61779-480-3_24

    *****************************************************


If the IDP model is selected, the output will be similar:

::

    t1t2ne makelists --MW 14.4 --Larmor 600 --idp


Which will provide the following output:

.. code-block:: console

    $ t1t2ne makelists --MW 14.4 --Larmor 600 --idp

    **************************************************
    *                                                *
    *                  T-one-T-tune                  *
    *                                                *
    *                makelists module                *
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

    No value provided for the xred parameter. Defaulting to [10, 30].
    TopSpin does not appear to be installed on a spectrometer workstation.
    Config file not found in the curdir folder of topspin for any of the users in the nmrsuperuser list.


    Estimated values for heteronuclear relaxation:

    expected T1 = 1.091 s
    expected T2 = 0.349 s
    expected hetnOe = 0.390
    Set the recovery delay for the hetnOe experiment in the range 4.363 - 6.544.

    Creating vdlist with 8 points and vclist with 8 points...


    The longest delay for the T1 experiment for a residual signal of 10% should be 2.51 s.

    vdlist for T1 experiment:
    -------------------------
    20.00u
    0.36000
    0.72000
    1.08000
    1.44000
    1.80000
    2.16000
    2.52000
    Using ".idp" sequence, which is optimized for long T2 times. d21 = 750u
    Enter the d21 value in microseconds (default 750): 
    Enter the p30 value in microseconds (default 160): 
    With the chosen d21 and p30 values, the maximum CPMG block allowed by the duty cycle is 0.64 s.
    Warning: the CPMG block of 0.03 s is too long for the T2 timescale, switching off the  "small" option
    The longest CPMG block for T2 for a residual signal of 30% should be 0.42 s, with 24 loops.
    Check if this is too long for your equipment before running the experiment

    vclist for T2 experiment:
    -------------------------
    0
    3
    6
    10
    13
    17
    20
    24



    *****************************************************

    Analysis complete. Below are the references for the methods used in this software.
    We can not nor we want to force you to cite any of these papers, but we - and likewise (we believe) the authors of the original papers - appreciate if you do.
    - Cavanagh, J., Fairbrother, W. J., Palmer III, A. G., Rance, M., & Skelton, N. J. (2007). Protein NMR spectroscopy: principles and practice. Academic Press. DOI: 10.1016/B978-0-12-164491-8.X5000-3

    - Rezaei‐Ghaleh, N., Parigi, G., Soranno, A., Holla, A., Becker, S., Schuler, B., ... & Zweckstetter, M. (2018). Local and global dynamics in intrinsically disordered synuclein. Angewandte Chemie International Edition, 57(46), 15262-15266. DOI: 10.1002/anie.201808172

    - Fushman, D. (2012). Determining Protein Dynamics from 15N Relaxation Data by Using DYNAMICS. In: Shekhtman, A., Burz, D. (eds) Protein NMR Techniques. Methods in Molecular Biology, vol 831. Humana Press. DOI: 10.1007/978-1-61779-480-3_24

    *****************************************************


As mentioned earlier, this script is more appropriately run following the a TRACT experiment. Taking as example the ubiquitin data described below in :ref:`sec;tract`:

::

    t1t2ne makelists --tau 4.57e+00 --S2 0.90 --Larmor 600


Likewise, after the synuclein TRACT experiment described in :ref:`sec;tract`:

::

    t1t2ne makelists --tau 8.80e+00 1.49e+00 --S2 0.15 0.38 --Larmor 600


The software accepts several command line options to customize the procedure:

-   Parameters related to the acquisition of the experiments:

    -   ``--xred``: the percent residual signal for the longest delay of the experiments. If not set, it will defaulto to 5% and 10% for T\ :sub:`1`\ and T\ :sub:`2`\  respectively.
    -   ``--nT``: the number of increments in the suggested vdlist for the T\ :sub:`1`\  experiment and T\ :sub:`1`\  T\ :sub:`2`\  experiments. Default is 8. If more than one value is provided, the first one will be used for the T\ :sub:`1`\  experiment, and the second one for the T\ :sub:`2`\  experiment.
    -   ``--logscale``: whether to use a logarithmic scale for the vdlist and vclist. Default is False, which means a linear scale will be used.
    -   ``--randomize``: whether to randomize the order of the values in the lists. Default is False.
    -   ``--Larmor``: the Larmor frequency of the spectrometer, in MHz. It will anyway be read from the configuration file of the spectrometer.
    -   ``--B0``: the magnetic field strength of the spectrometer, in Tesla. It will anyway be read from the configuration file of the spectrometer.
    -   ``--large``: whether to create the lists for the "large" sequence, which is optimized for short T2 times. Default is False.
    -   ``--small``: whether to create the lists for the "small" sequence, which is optimized for long T2 times. Default is False.

-   Parameters related to the estimation of the correlation times and order parameters:

    -   ``--S2``: the Lipari-Szabo order parameter S2 to use for the calculation of tau_c. In IDP mode, two values should be provide, else only one
    -   ``--MW``: the molecular weight of the protein in kDa, to be used for estimating the longest correlation time (tau_slow in the IDP model).
    -   ``--tau``: the correlation times to use for the estimation of the initial delays. In IDP mode, two values should be provided, else only one. If not set, they will be estimated from the MW. Otherwise, default T\ :sub:`1`\ and T\ :sub:`2`\  values will be used for the non-IDP model, and the three-tau model described in `Rezaei-Galeh et al.`_ for the IDP model.
    -   ``--idp``: whether the system under study is an intrinsically disordered protein (IDP). If set, the software will use the three-tau model described above. Default is False.

        -   If set, it will also select a longer delay in the cpmg for the T\ :sub:`2`\  experiment, optimized for the expected relaxation behavior of IDPs as described by `Bolognesi et al.`_.
        -   If set, it will also select a longer delay for the T\ :sub:`1`\  experiment, to avoid excessive heating, because cross-correlations are less important in IDPs.
        -   the ``--MW`` argument will be used to compute the slowest correlation time.
        -   ``--corr_window_idp``: the length of the correlation window for the IDP model, in residues. Default is 20.

    -   ``--T``: the temperature in Kelvin, to be used for estimating the taus from MW. Default is 298 K.

-   Parameters related to relaxation:

    -   ``--r``: the length of the 1H-15N bond in Angstroms. Default is 1.02 A.
    -   ``--Deltasigma``: the chemical shift anisotropy of the 15N nucleus in ppm. Default is -160 ppm.
    -   ``--nucs``: the nuclei to use for the calculation of the relaxation rates. Default is 1H and 15N.

.. _Bolognesi et al.: https://doi.org/10.1016/j.pnmrs.2025.101577
.. _Rezaei-Galeh et al.: https://doi.org/10.1002/anie.201808172



.. seealso:: 

   :class:`t1t2ne.scripts.t1t2ne_makelists`
