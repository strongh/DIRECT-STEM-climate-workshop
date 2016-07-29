"""
Example script using netCDF4 and numpy to read CCSM4 SIT data

Source    : https://pcmdi.llnl.gov/search/cmip5/
Author    : Zachary Labe
Date      : 29 June 2016
"""

### Import modules
import datetime
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

### Directory
directorydata = '/Users/zlabe/desktop/workshop/'
directoryfigure = '/Users/zlabe/desktop/workshop/'

### Time
now = datetime.datetime.now()
currentmn = str(now.month)
currentdy = str(now.day)
currentyr = str(now.year)
currenttime = currentmn + '/' + currentdy + '/' + currentyr
print '\n' '--- Sample SIT Script (%s) ---' '\n' % currenttime

def readSIT(directory,scenario):
    """
    Read SIT from netCDF4 file
    
    Parameters
    ----------
    directory : file path for data 
    scenario  : historical, rcp
    
    Returns
    -------
    lats      : 50N- latitude
    lons      : 0-360 longitude
    sit       : sea ice thickness (meters)
    """
    
    filename = 'sit_grid50N_CCSM4_rcp85_1.nc'
    
    data = Dataset(directory + filename)
    lats = data.variables['lat'][:]
    lons = data.variables['lon'][:]
    sit = data.variables['sit'][:]
    data.close()
    
    if scenario == 'historical':
        years = 2006 - 1850 # years 1850-2005
    elif scenario == 'rcp':
        years = 2101 - 2006 # years 2006-2100
    
    ### Reshape [year,month,lat,lon]
    sit = np.reshape(sit,(years,12,lats.shape[0],lons.shape[1]))
    
    print 'Completed: Read sit data!'
    return lats,lons,sit
    
### Call functions
lats,lons,sit = readSIT(directorydata,'rcp')

###########################################################################
###########################################################################

### Plot sit
fig = plt.figure()
ax = plt.subplot(111)
m = Basemap(projection='ortho',lon_0=-90,lat_0=70,resolution='l',
            round=True) # map projection either this or npstere
m.drawmapboundary(fill_color='w')
m.drawcoastlines(color='darkgrey',linewidth=0.5)
parallels = np.arange(50,90,10)
meridians = np.arange(-180,180,30)
m.drawparallels(parallels,label=[False,False,False,False],
                linewidth=0.5,color='k',fontsize=9)
m.drawmeridians(meridians,labels=[False,False,False,False],
                linewidth=0.5,color='k',fontsize=9)
m.drawlsmask(land_color='darkgrey',ocean_color='mintcream')

### adjust limits
sit[np.where(sit > 8.)] = np.nan
sit[np.where(sit == 0.)] = np.nan
info = 'Sea Ice Thickness'

### Plot filled contours (for year 2006, March)
cs = m.contourf(lons,lats,sit[0,2,:,:],np.arange(0,8.5,0.5),
                latlon=True,extend='max')

### Set colormap
cs.set_cmap('inferno')

### Set colorbar
cbar = m.colorbar(cs,drawedges=True,location='right',pad=0.2)
cbar.set_ticks(np.arange(0,8.1,1))
cbar.set_label('Thickness (m)')

### Set title
fig.suptitle('Sea Ice Thickness, March 2006',fontsize=14)

### Save figure
plt.savefig(directoryfigure + 'example_sit.png',dpi=300)
print 'Completed: Plot finished!'

print 'Completed: Script done!'