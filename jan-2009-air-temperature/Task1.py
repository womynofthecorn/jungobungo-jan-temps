from netCDF4 import Dataset
nc = Dataset('ta_2m_1hr_20090101_d02.nc', 'r')
for i in nc.variables:
    print(i, nc.variables[i].units, nc.variables[i].shape)
