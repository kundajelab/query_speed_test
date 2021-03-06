

# query_speed_test
testing querying various backends (i.e. tiledb, hdf5, bigwig) 

## to automatically time the execution of each cell in jupyter notebook: 
```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable execute_time/ExecuteTime
```

## Dependencies:
```
pip show tiledb 
Name: tiledb
Version: 0.6.6
Summary: Pythonic interface to the TileDB array storage manager
Home-page: https://github.com/TileDB-Inc/TileDB-Py
Author: TileDB, Inc.
Author-email: help@tiledb.io
License: MIT
Requires: numpy, wheel


pip show h5py 
Name: h5py
Version: 2.10.0
Summary: Read and write HDF5 files from Python
Home-page: http://www.h5py.org
Author: Andrew Collette
Author-email: andrew.collette@gmail.com
License: BSD
Requires: numpy, six

pip show pyBigWig
Name: pyBigWig
Version: 0.3.17
Summary: A package for accessing bigWig files using libBigWig
Home-page: https://github.com/dpryan79/pyBigWig
Author: Devon P. Ryan
Author-email: ryan@ie-freiburg.mpg.de
License: UNKNOWN

pip show numpy 
Name: numpy
Version: 1.18.1
Summary: NumPy is the fundamental package for array computing with Python.
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email: None
License: BSD
```
## Download test datasets: untar/unzip:
### tiledb hg38, ENCSR000EID
```
wget http://mitra.stanford.edu/kundaje/annashch/query_speed_test/ENCSR000EID.tdb.tgz
tar -xzvf ENCSR000EID.tdb.tgz
```
### hdf5 hg38, ENCSR000EID
```
wget http://mitra.stanford.edu/kundaje/annashch/query_speed_test/ENCSR000EID.hdf5
```
### pyBigWig
```
wget http://mitra.stanford.edu/kundaje/annashch/query_speed_test/ENCSR000EID.merged.nodup.fc.signal.bigwig
```

## numpy array #large file - 24G 
``` 
wget http://mitra.stanford.edu/kundaje/annashch/query_speed_test/ENCSR000EID.npy 
```
## run query_speed_test_LOCAL.ipynb to benchmark tiledb vs hdf5 vs pyBigWig
