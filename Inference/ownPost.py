import matplotlib.pyplot as plt
import numpy as np
from pycbc.io import InferenceFile

#Iteration to plot
iteration=4999
num_walkers=5000

#Read in file
datafile="20170228-225207/output.hdf"
fp = InferenceFile("%s" % datafile, "r")

parameter_values=np.zeros(num_walkers)

for aa in range(num_walkers):
   samples = fp.read_samples("mchirp", walkers=0)
   temp=samples.mchirp
   parameter_values[aa]=temp[iteration]

plt.figure()
plt.hist(parameter_values,200)
plt.xlabel("Chirp mass")
plt.show("hold")

