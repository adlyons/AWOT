# -*- coding: utf-8 -*-
"""
RadarDataFile.py - Class for reading Data from file
"""
#import io.read_p3_2dimage_probe as ReadData
import os

#from ..AirborneData import AirborneData
from ..io.read_ground_radar import read_radar as read_ground_radar
#from ..io.read_tdr_grid import read_dpj_netcdf_grid_basic as read_tdr_grid
from ..io.read_p3_radar import read_lf_grid, read_dpj_tdr_grid_netcdf, read_tdr_sweep


import numpy as np
########################
## BEGIN MAIN CODE
########################

def read_radar(filename=None, platform='p3', file_format='netcdf', instrument=None,
               data_format='grid', initialize=False ):
    '''
    Takes a filename pointing to a aircraft flight level data file
     and returns a FlightLevel object.
        
    Parameters::
    ------------
    filename : str
        Long path filename of data file.
    platform : str
        Platform for processing, see FileReader.
    file_format : str
            Format of input file, see FileReader.
        instrument : str
            Type (name) of instrument to process
            Currently the following arguments are valid:
                'tdr_grid' - Tail Doppler radar gridded files (e.g. dual-Doppler analysis)
                'tdr_sweep' = Tail Doppler radar (Native coordinate data)
                'lf'  - Lower Fuselage radar
                'ground' - A ground-based radar system, read in using PyArt
    data_format : str
        Either 'grid' or 'native'.
    To Do:
    Add support for:
        Eldora X-band (historical) - should be similar to P3
        King Air/C-130 95 GHZ
        
    '''
    if filename is None:
        print "Need to provide a filename!"
        return
    
    reader = FileReader(filename=filename, platform=platform, 
                        file_format=file_format, instrument=instrument)
    
    if initialize:
        RadarData = AirborneData(reader)
    
        return RadarData
    else:
        return reader
###################################################

class FileReader(object):

    '''
    FileReader class to process data files.  
    '''
    
    def __init__(self, filename=None, platform=None, file_format='netcdf',
                 instrument=None):

        """
        If initialized with a filename (incl. path), will call
        ***_read_flight() to populate the class instance.
        If not, it simply instances the class but does not populate
        its attributes.
        verbose: Set to True for text output. Useful for debugging.
        
        OPTIONAL INPUT::
            filename : string
                Filename (including path) of file to process
            platform : string
                Name of aicraft 
                Currently supported: 
                    'p3' or p-3' (NOAA WP-3D)
                    I
                    'citation' (Univ North Dakota Citation)
            file_format : string
                Format of input file.  Each platform currently has
                a specific file type.  This may be extended in the future.
                Currently supported:
                    'netcdf'
                    'ascii'
            instrument : str
                'tdr_grid' - Tail Doppler radar gridded files (e.g. dual-Doppler analysis)
                'tdr_sweep' = Tail Doppler radar (Native coordinate data)
                'lf'  - Lower Fuselage radar
                'ground' - A ground-based radar system, read in using PyArt
        
        """

        if isinstance(filename, str) != False:
            
            if instrument is None:
               print "Need to supply instrument type"
               return
            if instrument.lower() == 'ground':
                radar = read_ground_polar(filename)
            elif instrument.lower() == 'lf':
                if (platform.upper() == 'P3') or (platform.upper() == 'P-3'):
                    radar = read_lf_grid(filename)
            elif instrument.lower() == 'tdr_grid':
                if (platform.upper() == 'P3') or (platform.upper() == 'P-3'):
                    if file_format.lower() =='netcdf':
                        radar = read_dpj_tdr_grid_netcdf(filename)
            elif instrument.lower() == 'tdr_sweep':
                if (platform.upper() == 'P3') or (platform.upper() == 'P-3'):
                    if file_format.lower() =='netcdf':
                        radar = read_tdr_sweep(filename)
            else:
                print "Check the supported instrument list"
                return
                
            
            if (platform.upper() == 'ELDORA'):
                print "Sorry not supported at this time"
            elif (platform.upper() == 'C130') or (platform.upper() == 'KING AIR'):
                print "Sorry not supported at this time"
            
#             if (platform.upper() == 'P3') or (platform.upper() == 'P-3'):
#                 if file_format.upper() == 'NETCDF':
#                     if instrument == 'tdr_sweep':
#                         flight = p3_read_tdr_sweep(filename)
#                     if instrument == 'tdr_grid':
#                         flight = p3_read_grid(filename)
#                     if instrument == 'lf':
#                         flight = p3_read_lf(filename)
#             elif (platform.upper() == 'ELDORA'):
#                 print "Sorry not supported at this time"
#             elif (platform.upper() == 'C130') or (platform.upper() == 'KING AIR'):
#                 print "Sorry not supported at this time"
#             else:
#                     print "Check the format call!"
#                     return
                    
            
            # Record the data into the variable 
            self.radar_data = radar
            
        else:
            #Initializes class instance but leaves it to other methods to
            #populate the class attributes.
            return 
            

            
        