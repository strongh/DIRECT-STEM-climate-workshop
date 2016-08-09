"""

Function has plotting routine for Arctic polar map using Python's Basemap
with options for different map projections.

Notes
-----

    Workshop : DIRECT-STEM Climate Workshop 
              (https://github.com/strongh/DIRECT-STEM-climate-workshop)
    Author : Zachary Labe
    
Usage
-----
    plotMap(projection)
    
"""

def plotMap(projection):
    """
    Function is plotting utility for Arctic or global maps
    
    Parameters
    ----------
    projection : string
        ortho, polar
        
    Returns
    -------
    m : basemap utility with selected parameters
        
    Usage 
    -----
    plotMap('polar')
    """
    
    ### Import Modules
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap
    
    ### Select map projection
    if projection == 'ortho':
        m = Basemap(projection='ortho',lon_0=-90,
                    lat_0=70,resolution='l',round=True)
    elif projection == 'polar':
        m = Basemap(projection='npstere',boundinglat=66,lon_0=270,
                    resolution='l',round =True)
    else:
        ValueError('entered wrong map projection!')
    
    ### Draw coastlines
    m.drawmapboundary(fill_color='white')                
    m.drawcoastlines(color='k',linewidth=0.8)
    
    ### Draw parallels and meridians
    if projection == 'ortho':
        parallels = np.arange(50,90,10)
        meridians = np.arange(-180,180,30)    
        m.drawparallels(parallels,labels=[False,False,False,False],
                        linewidth=0.5)
        m.drawmeridians(meridians,labels=[False,False,False,False],
                        linewidth=0.5,fontsize=8)
    elif projection == 'polar':
        parallels = np.arange(50,90,10)
        meridians = np.arange(-180,180,30)    
        m.drawparallels(parallels,labels=[False,False,False,False],
                        linewidth=0.5)
        m.drawmeridians(meridians,labels=[True,True,False,False],
                        linewidth=0.5,fontsize=8)
    else:
        ValueError('entered wrong map projection!')
    
    ### Fill in land and ocean color                
    m.drawlsmask(land_color='darkgrey',ocean_color='mintcream')                
    
    return m 
    
###########################################################################
###########################################################################
### Example syntax:
#Basemap projection polar stereographic
#m = plotMap('polar')