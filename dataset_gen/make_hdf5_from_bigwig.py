import pyBigWig
import pandas as pd
import h5py
import pdb
import numpy as np 

data=pyBigWig.open("ENCSR000EID.merged.nodup.fc.signal.bigwig",'r')
chromsizes=pd.read_csv("hg38.chrom.sizes",header=None,sep='\t')
chrom_dict=dict()
for index,row in chromsizes.iterrows():
    chrom=row[0]
    size=row[1]
    chrom_dict[chrom]=np.nan_to_num(data.values(chrom,0,size))
    print("got values for chrom "+str(chrom))

#store to hdf5
with h5py.File("ENCSR000EID.hdf5",'w') as cur_f:
    for chrom in chrom_dict:
        cur_f.create_dataset(chrom,data=chrom_dict[chrom],dtype='f')
        print('wrote:'+chrom)
    
        
        
    
