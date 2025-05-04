import os
import pandas as pd
from functools import cache
import timeit

# Data file paths
curr_path = os.path.dirname(os.path.realpath(__file__))
dir_aircraft = os.path.join(os.path.dirname(os.getcwd()), "data", "aircraft")
simplifiedProps_dir = os.path.join(dir_aircraft, "AircraftDB_Standard_Props.ssv")
simplifiedJets_dir = os.path.join(dir_aircraft, "AircraftDB_Standard_Jets.ssv")

@cache
def available_aircrafts(ac_type= None):
    """Return the available aircrafts"""
    
    # Load the data
    simplified_props = pd.read_csv(simplifiedProps_dir, sep=";")
    simplified_jets = pd.read_csv(simplifiedJets_dir, sep=";")
    
    aircraft_map = {
        "Simplified Propeller": simplified_props["name"],
        "Simplified Jet": simplified_jets["name"],
        "Any": pd.concat([simplified_props["name"], simplified_jets["name"]])
    }
    
    return list(aircraft_map.get(ac_type, []))
    

class Aircrafts:
    def __init__(self, ac_type, ac_name):
        
        self.ac_data = None
        raise NotImplementedError
    
    
