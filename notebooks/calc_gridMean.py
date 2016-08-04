"""
Function calculates gridded mean for oceanic or land grids from CMIP5 files

Notes
-----
    Data : https://pcmdi.llnl.gov/search/cmip5/
    Workshop : DIRECT-STEM Climate Workshop 
              (https://github.com/strongh/DIRECT-STEM-climate-workshop)
    Author : Zachary Labe
"""
   
def calcYearMean(vari,area):
    """
    Function calculates areal mean for CMIP5 variables taking into account
    grid cell area and land/ocean masks, which corrects the mean to a more
    realistic value
    
    Parameters
    ----------
    vari : 4d array [year,month,lat,lon]
        variable from CMIP5 for land or ocean grids
    area : 2d array
        areacella or areacello
        
    Returns
    -------
    varmean : 1d array
        time weighted average
    """
    import numpy as np
    
    vari = np.reshape(vari,(vari.shape[0]*vari.shape[1],
                            vari.shape[2],vari.shape[3]))
    
    ### Create a variable to hold the years
    nyears = int(vari.shape[0]/12.)
    
    ### Create some arrays using numpy to hold the variable means
    varyearmean = np.zeros((nyears, vari.shape[1], vari.shape[2]))
    variyr = np.zeros(nyears)
    
    ### Average all the vari during an individual year 
    for i in xrange (nyears):
        varyearmean = np.average(vari[i*12:i*12+12,:,:], axis = 0)
        variyr[i] = np.nansum(varyearmean*area)/np.nansum(area)
    return variyr    
