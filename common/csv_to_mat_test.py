import os
import pandas as pd
import scipy


filep='file'
basename=os.path.basename(filep)
data = pd.io.read_csv(basename+".csv",parse_dates=True)
scipy.io.savemat(basename+'.mat',data)