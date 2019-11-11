import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from mpl_toolkits.basemap import Basemap
import matplotlib
matplotlib.use("Agg")
nc = Ncdf('ta_2m_1hr_20090101_d02.nc', 'r')
print(nc)
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
lons = nc.variables['lon'][:]
lats = nc.variables['lat'][:]
time = nc.variables['time'][:]
t2 = nc.variables['ta_2m'][:]
map = Basemap(projection='merc', llcrnrlon=lons[0], llcrnrlat=lats[0], urcrnrlon=lons[599], urcrnrlat=lats[698],
             resolution='i')
#map.drawcoastlines()
# map.drawstates()
#map.drawcountries()
#map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF')
lon2, lat2 = np.meshgrid(lons, lats)
x, y = map(lon2, lat2)
my_cmap = plt.get_cmap('RdBu_r')
my_cmap.set_under('white')
map.pcolormesh(x, y, t2[0, :, :], cmap='RdBu_r')
plt.colorbar(label="Temperature (K)")
for b in range(0, 744):
    map.pcolormesh(x, y, t2[b, :, :], cmap='RdBu_r')
    plt.title('2m Temperature')
    plt.savefig("E:/elise/Documents/JungoBunbo/jan-2009-air-temperature/ta2m_%s.png" % b)
