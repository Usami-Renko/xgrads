# -*- coding: utf-8 -*-
"""
Created on 2020.03.02

@author: MiniUFO
Copyright 2018. All rights reserved. Use is subject to license terms.
"""
import numpy as np
import xarray as xr
from xgrads import open_CtlDataset, open_mfdataset


def test_template():
    dset1 = open_CtlDataset('./ctls/test8.ctl')
    dset2 = open_CtlDataset('./ctls/test9.ctl')
    dset3 = xr.tutorial.open_dataset('air_temperature')
    
    for l in range(len(dset1.time)):
        xr.testing.assert_equal(dset1.air[l], dset2.air[l])
        xr.testing.assert_equal(dset1.air[l], dset3.air[l])

    
    dset1 = open_mfdataset('./ctls/test8_*.ctl', parallel=True)
    dset2 = open_CtlDataset('./ctls/test8.ctl').load()
    dset3 = xr.tutorial.open_dataset('air_temperature').load()
    
    for l in range(len(dset1.time)):
        xr.testing.assert_equal(dset1.air[l], dset3.air[l])
    
    
    dset1 = open_mfdataset('./ctls/test9_*.ctl', parallel=True)
    dset2 = open_CtlDataset('./ctls/test9.ctl').load()
    dset3 = xr.tutorial.open_dataset('air_temperature').load()
    
    for l in range(len(dset1.time)):
        xr.testing.assert_equal(dset1.air[l], dset2.air[l])
    
    
    # test blank line in ctls
    dset1 = open_CtlDataset('./ctls/test81.ctl')
    dset2 = open_CtlDataset('./ctls/test82.ctl')
    
    assert (dset1.x == dset2.x).all()
    assert (dset1.y == dset2.y).all()
    assert (dset1.air[0] == dset2.air).all()

def test_ensemble():
    dset1 = open_CtlDataset('./ctls/ecmf_medium_T2m1.ctl')
    
    expected = np.array([2.011963 , 1.1813354, 1.1660767])
    
    # check several ensemble values
    assert np.isclose(dset1.t2[:,-1,-1,-1], expected).all()
