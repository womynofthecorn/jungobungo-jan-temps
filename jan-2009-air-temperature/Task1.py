import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from netCDF4 import Dataset
import mpl_toolkits.basemap as bm
sns.set()
nc = Dataset('ta_2m_1hr_20090101_d02.nc', 'r')
print(nc)
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)

lon = nc.variables['lon'][:]
lat = nc.variables['lat'][:]
time = nc.variables['time'][:]
lons,lats = np.meshgrid(lon-180,lat)
map = bm.Basemap(projection='merc', llcrnrlon=-93.,llcrnrlat=35.,urcrnrlon=-73.,urcrnrlat=45.,resolution='i')
x,y = map(lons,lats)
temp = map.contourf(x,y,t2[4, :, :])
plt.title('2m Temperature')
cb.set_label('Temperature (K)')
plt.show()
cb = map.colorbar(temp,"bottom", size="5%", pad="2%")
plt.savefig("E:/elise/Documents/JungoBunbo/jan-2009-air-temperature/figure.png", 100)
zip()