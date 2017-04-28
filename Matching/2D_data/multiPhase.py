import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pickle
import numpy as np

fname="phase_s20psi1"
fname2="phase_s20psi2"
fname3="phase_s20psi3"
fname4="phase_s20psi4"


#Data saved in the form of x values, y values, z values
x,y,z,specs=pickle.load(open("%s.p" % fname,"rb"))
x2,y,z,specs=pickle.load(open("%s.p" % fname2,"rb"))
x3,y,z,specs=pickle.load(open("%s.p" % fname3,"rb"))
x4,y,z,specs=pickle.load(open("%s.p" % fname4,"rb"))
m1=specs[0]
m2=specs[1]

plt.figure()
plt.subplot(2,2,1)
plt.contourf(x,y,z,200,cmap="inferno")
plt.colorbar()
plt.ylabel("Phase")
plt.subplot(2,2,2)
plt.contourf(x2,y,z,200,cmap="inferno")
plt.colorbar()
plt.subplot(2,2,3)
plt.contourf(x3,y,z,200,cmap="inferno")
plt.colorbar()
plt.xlabel("Inclination")
plt.ylabel("Phase")
plt.subplot(2,2,4)
plt.contourf(x4,y,z,200,cmap="inferno")
plt.colorbar()
plt.xlabel("Inclination")
plt.show("hold")
plt.savefig("multi.png")
print "DONE"
