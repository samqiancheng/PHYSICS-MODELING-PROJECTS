from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
#from math import factorial
from scipy.special import factorial
from scipy.signal import convolve
def Poisson(r,lam):
    return(np.power(lam,r)*np.exp(-lam)/factorial(r))


def gaussian(x,x0,a):   # this defines a normalized gaussian function
    return( np.exp(-(x-x0)**2/(2.0*a**2))/np.sqrt(2.0*np.pi*a**2))   # note that the math functions and pi are contained in the numpy library

zerolist=[]      
for i in range(1,10):
    hdulist = fits.open(str(i)+'BIAS.fits')
    zeroarr = hdulist[0].data
    zerolist.append(zeroarr)
    hdulist.close()

bigzero = np.dstack(zerolist)

zeroframe = np.mean(bigzero,axis=2)

hdulist = fits.open('Dark40.fits')
darkarr= hdulist[0].data
redarr=darkarr-zeroframe
bins= range(-20,40)
plt.hist(np.ravel(redarr), bins,normed='True')
#plt.show()


#print(np.mean(bigzero(100,100,:)),np.std(bigzero(100,100,:)))
#hdulist = fits.open('Dark120.fit')
#dark40arr = hdulist[0].data
#hdulist.close()

#redim= np.abs(dark40arr - zeroarr)



#bins= range(0,40)
#plt.hist(np.ravel(redim), bins,normed='True')

xlist = np.arange(-20,50,0.01)
ylist = Poisson(xlist,2.4)
ylist[ylist==np.inf]=0
zlist = gaussian(np.arange(0,40,0.01),20,8)
conlist = convolve(ylist,zlist,mode='same')/100
plt.plot(xlist,conlist)
plt.show()


