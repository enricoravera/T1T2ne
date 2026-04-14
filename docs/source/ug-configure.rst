.. _sec;configure:

Getting started on a spectrometer workstation
*********************************************

This section describes the recommended first-time setup of **T1T2ne** on a Bruker TopSpin spectrometer workstation. The goal is to let the software automatically discover instrument parameters (e.g. field strength) and to store a *default dataset location* that can be reused by the TRACT and NS modules.

The workflow has two phases:

1. **One-time configuration** (performed by an NMR superuser).
2. **Day-to-day usage** (performed by any user running `t1t2ne`).

.. warning::

   The command ``t1t2ne configure`` writes a configuration file inside the TopSpin installation (in the ``prog/curdir/<user>/`` area). For this reason it can only be run by a user listed in the TopSpin ``nmrsuperuser`` file. If you are not a superuser, ask the local NMR facility staff to run the configuration step once.

Prerequisites
-------------

- Python >= 3.10 must be available on the workstation.
- TopSpin must be installed locally on the workstation.
- For the *configuration step only*: you must be an NMR superuser (TopSpin admin).

Installation (NMR superuser)
----------------------------

Install the software as described in the `Installation guide`_. On a linux workstation, we have installed miniconda in the /opt/miniconda3 directory, and then installed T1T2ne in a conda environment named `t1t2ne` with the command:

::

    conda create --name t1t2ne python=3.10
    conda activate t1t2ne
    pip install t1t2ne

At the end of the installation, for each user, you can initialize conda and the enviroment with:

::

    /opt/miniconda3/bin/conda init bash
    conda activate t1t2ne

One-time configuration (NMR superuser)
--------------------------------------

Run the configuration command from a terminal:

::

    t1t2ne configure

The program will:

- locate the local TopSpin installation (or you can provide it explicitly, see below),
- ask for a **standard dataset directory** (a dataset you want to use as default example/reference),
    - can be specified with ``--basedir`` (dataset directory),   
- ask for the experiment number of a **TRACT** experiment
    - can be specified with - ``--tract`` (TRACT experiment number), 
- verify that the selected TRACT experiment is actually a TRACT experiment (by inspecting the pulse program name),
- ask for the experiment number of an **HSQC** experiment within that dataset,
    - can be specified with ``--hsqc`` (HSQC experiment number, used by the ``ns`` module).
- write a configuration file named ``tract_analysis_config.ini`` in the TopSpin *curdir* for the current user.

.. note::

    *curdir* is a TopSpin concept that refers to a user-specific directory which is carried over across successive TopSpin installations.

The resulting config is used by T1T2ne to pre-fill the default values for dataset location and experiment numbers for the test datasets, to be used as a reference for the users.


If TopSpin is not found automatically, or if you want to force a specific path, you can provide it:

::

    t1t2ne configure --topspinpath /opt/topspin4

(Replace the path with the local TopSpin installation directory on your system.)


Day-to-day usage on the spectrometer
------------------------------------

Once the configuration file exists, most commands can be run with minimal arguments, because the software will reuse the defaults recorded in ``tract_analysis_config.ini``.

Troubleshooting
---------------

**Problem:** ``TopSpin does not appear to be installed on this workstation``  
**Cause:** T1T2ne could not locate TopSpin.  
**Fix:** run ``t1t2ne configure --topspinpath <path>`` (superuser) or contact facility staff.

**Problem:** ``Only the NMR superuser can write the config file. Exiting.``  
**Cause:** you are not listed in TopSpin ``nmrsuperuser``.  
**Fix:** ask facility staff (superuser) to run ``t1t2ne configure`` once.

**Problem:** ``Experiment <N> is not a TRACT experiment``  
**Cause:** the selected experiment does not appear to be a TRACT dataset (based on pulse program inspection).  
**Fix:** double-check the experiment number and confirm the TRACT sequence name used on your system contains the substring ``tract``.