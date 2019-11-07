import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset as Ncdf
from mpl_toolkits.basemap import Basemap
nc = Ncdf('ta_2m_1hr_20090101_d02.nc', 'r')
print(nc)
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]
time = nc.variables['time'][:]
t2 = nc.variables['2m'][:]
map = Basemap(projection='merc',llcrnrlon=-93.,llcrnrlat=35.,urcrnrlon=-73.,urcrnrlat=45.,resolution='i')
map.drawcoastlines()
map.drawstates()
map.drawcountries()
map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF')
lon, lat = np.meshgrid(lon-180, lat)
x, y = map(lon, lat)
temp = map.contourf(x, y, t2[4,:, :])
cb = map.colorbar(temp,"bottom", size="5%", pad="2%")
plt.title('2m Temperature')
cb.set_label('Temperature (C)')
plt.show()
plt.savefig("E:/elise/Documents/JungoBunbo/jan-2009-air-temperature/figure.png", 100)

