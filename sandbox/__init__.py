"""
Module initialisation for sandbox
Created on 15/04/2020

@author: Simon Virgo, Daniel Escallon, Miguel de la Varga
"""
# Main information for all the modules to work (calibration data, projector and sensor)
import os
#from . import projector, sensor, markers, calibration, modules

_test_data = {'topo': os.path.dirname(__file__) +
                       '/../notebooks/tutorials/06_LoadSaveTopoModule/saved_DEMs/',
              'landslide_topo': os.path.dirname(__file__) +
                                '/../notebooks/tutorials/07_LandslideSimulation/saved_DEMs/',
              'landslide_release': os.path.dirname(__file__) +
                                   '/../notebooks/tutorials/07_LandslideSimulation/saved_ReleaseAreas/',
              'landslide_simulation': os.path.dirname(__file__) +
                                   '/../notebooks/tutorials/07_LandslideSimulation/simulation_data/',
              'gempy_data': os.path.dirname(__file__) +
                            '/../notebooks/tutorials/04_GempyModule/Example_Models/inputdata/'}

_calibration_dir = os.path.dirname(__file__) + '/../notebooks/calibration_files/'

#from .main_thread import MainThread


if __name__ == '__main__':
    pass
