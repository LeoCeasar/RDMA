#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import numpy as np
import sys
print(sys.argv)

np.set_printoptions(7)
data = np.random.rand(1 if len(sys.argv)==1 else int(sys.argv[1]), 2000)
np.savetxt("rand.csv" if len(sys.argv)<3 else sys.argv[2], data, delimiter=",")



