#! /usr/bin/env python3

"""
Registry dei sottocomandi.

"""

from t1t2ne.scripts.t1t2ne_configure import ConfigureCmd
from t1t2ne.scripts.t1t2ne_makelists import MakeListsCmd
from t1t2ne.scripts.t1t2ne_setuptract import SetupTractCmd
from t1t2ne.scripts.t1t2ne_tract import TractCmd
from t1t2ne.scripts.t1t2ne_ns import NSCmd
from t1t2ne.scripts.t1t2ne_interactive import InteractiveCmd
from t1t2ne.scripts.t1t2ne_solventpre import SPREListsCmd

registry = {
    "makelists": MakeListsCmd,
    "solventpre": SPREListsCmd,
    #"shuttle": ShuttleCmd,
    "setuptract": SetupTractCmd,    
    "configure": ConfigureCmd,
    "ns": NSCmd,    
    "tract": TractCmd,
    "interactive": InteractiveCmd,
}

