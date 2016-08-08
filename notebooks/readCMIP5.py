"""

Function reads cmip5 data for all variables and scenarios.

Notes
-----
    Data : https://pcmdi.llnl.gov/search/cmip5/
    Workshop : DIRECT-STEM Climate Workshop 
              (https://github.com/strongh/DIRECT-STEM-climate-workshop)
    Author : Zachary Labe
    
Usage
-----
    readCMIP5Data(directory,domain,simulation,ensemble,vari)
    
"""
   
def readCMIP5Data(directory,domain,simulation,ensemble,vari):
    """
    Function reads in cmip5 data using netCDF4 module with output as an 
    array.
    
    Parameters
    ----------
    directory : string
        working directory for cmip5 data
    domain : string
        global, gridded 
    simulation : string
        historical, rcp26, rcp45, rcp85
    ensemble : string
        1,2,3,4,5
    vari : string
        tas,tos,pr,psl,sic,sit,snd
        
    Returns
    -------
    var : 4d array
        tas,tos,pr,psl,sic,sit,snd [year,month,lat,lon]
        
    Usage 
    -----
    lats,lons,var = readCMIP5Data(directory,'gridded','historical','1','tas')
    """
    
    ### Assign modules
    import numpy as np
    from netCDF4 import Dataset
    
    ### Check for bugs in function entry
    ense = [vari=='psl',vari=='tos',vari=='sic',vari=='sit',vari=='snd']
    if any(ense) and ensemble !='1':
        print '\n You have been reassigned ensemble 1 for --> %s! \n' % (vari)
        ensemble = 1
    else:
        ensemble = ensemble
    
    ### Assign variable grids
    if domain == 'gridded':
        landgrid = [vari=='tas',vari=='pr',vari=='psl']
        oceangrid = [vari=='tos',vari=='sic',vari=='sit',vari=='snd']
        if any(landgrid):
            grid = 'grid65N'
        elif any(oceangrid):
            grid = 'grid50N'
        else:
            ValueError('variable naming error!')
    elif domain == 'global':
        grid = 'global'
    else:
        ValueError('wrong value for domain selected!')
    
    ### Assign file    
    filename = '%s_%s_CCSM4_%s_%s.nc' % (vari,grid,simulation,ensemble)
    
    ### Read in netcdf file
    data = Dataset(directory + filename)
    lats = data.variables['lat'][:]
    lons = data.variables['lon'][:]
    var = data.variables['%s' % (vari)][:]
    data.close()
    
    ### Select simulation
    rcps = [simulation=='rcp26',simulation=='rcp45',simulation=='rcp85']
    if simulation == 'historical':
        years = 156
    elif any(rcps):
        years = 95
    else:
        ValueError('wrong simulation selected!')
    ### Reshape array 
    var = np.reshape(var,(years,12,lats.shape[0],lons.shape[0]))
    
    return lats,lons,var

###########################################################################
###########################################################################
### Example syntax:
#CCSM4 surface air temperature, Arctic grid, historical, ensemble 1
#
#directory = '../Data/'
#lats,lons,var = readCMIP5Data(directory,'gridded','historical','1','tas')


def readUtilityData(directory,domain,vari):
    """
    Function reads in utility CCSM4 geographical data using netCDF4 module with output as an 
    array.
    
    Parameters
    ----------
    directory : string
        working directory for cmip5 data
    domain : string
        global, gridded 
    ensemble : string
        1,2,3,4,5
    vari : string
        areacella,areacello,landfrac,oceanfrac
        
    Returns
    -------
    var : 4d array
        areacella,areacello,landfrac,oceanfrac [lat,lon]
        
    Usage 
    -----
    lats,lons,var = readCMIP5Data(directory,'gridded','tas')
    """
    
    ### Assign modules
    import numpy as np
    from netCDF4 import Dataset
    

    
    ### Assign variable grids
    if domain == 'gridded':
        landgrid = [vari=='areacella',vari=='landfrac']
        oceangrid = [vari=='areacello',vari=='oceanfrac']
        if any(landgrid):
            grid = 'grid65N_'
        elif any(oceangrid):
            grid = 'grid50N_'
        else:
            ValueError('variable naming error!')
    elif domain == 'global':
        grid = ''
    else:
        ValueError('wrong value for domain selected!')
    
    ### Assign file    
    filename = '%s_%sCCSM4.nc' % (vari,grid)
    
    ### Read in netcdf file
    data = Dataset(directory + filename)
    lats = data.variables['lat'][:]
    lons = data.variables['lon'][:]
    var = data.variables['%s' % (vari)][:]
    data.close()
    
    ### Reshape array 
    var = np.reshape(var,(lats.shape[0],lons.shape[0]))
    
    return lats,lons,var

###########################################################################
###########################################################################
### Example syntax:
#directory = '../Data/'
#lats,lons,var = readUtilityData(directory,'gridded','landfrac')

