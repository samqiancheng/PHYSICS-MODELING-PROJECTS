from astropy.io import fits
import numpy as np
from matplotlib.pyplot import *
from scipy.special import factorial
from scipy.signal import convolve

def printDash():
	print('--------------------------------')

def writeLog(string,n1,n2):
	print('|'+'{:^13}'.format(string)+'|'+'{:08.4f}'.format(n1)+'|'+'{:08.4f}'.format(n2)+'|')
	printDash()

def Poisson(r,lam):
    return(np.power(lam,r)*np.exp(-lam)/factorial(r))


def gaussian(x,x0,a):   # this defines a normalized gaussian function
    return( np.exp(-(x-x0)**2/(2.0*a**2))/np.sqrt(2.0*np.pi*a**2))   # note that the math functions and pi are contained in the numpy library

printDash()
print('|'+'{:^13}'.format('NAME')+'|'+'{:^8}'.format('MEAN')+'|'+'{:^8}'.format('STD')+'|')
printDash()

biaslist = []
for i in range(1,10):
	hdulist = fits.open("PoissonProject/Bias-"+str(i)+".fit")
	biasframe = hdulist[0].data
	biaslist.append(biasframe)
#	hdulist.info()
	hdulist.close()

#zero frame, (1472,2184)
zeroframe = np.mean(biaslist,axis=0)
writeLog('Bias Frame',np.mean(zeroframe),np.std(zeroframe))

#readout = biasframe - zeroframe
readout = biaslist - zeroframe
writeLog('Readout Noise',np.mean(readout),np.std(readout))
#print('mean of readout noise',np.mean(readout))
#print('std of readout noise',np.std(readout))

if np.mean(readout) > 0.0001:
	print("Error in readout std")

#quit()
title('Readout noise distriution')
hist(np.ravel(readout),range(-40,40),density=1)
xlim(-40,40)
gaussianx = np.arange(-40,40,0.01)
gaussiany = gaussian(gaussianx,0,9.63)
plot(gaussianx,gaussiany)

#Dark frames-------------------------
def read_dark_frame(exposure):
	hdulist = fits.open('PoissonProject/Dark-'+str(exposure)+'s.fit')
	result = hdulist[0].data - zeroframe
	#print("mean of exposure time",str(exposure),"is",np.mean(result))
	#print("std of exposure time",str(exposure),"is",np.std(result))
	writeLog('Exposure '+str(exposure)+'s',np.mean(result),np.std(result))
	return result
inf_red_10 = read_dark_frame(10)
inf_red_20 = read_dark_frame(20)
inf_red_60 = read_dark_frame(60)
inf_red_120 = read_dark_frame(120)
savefig('readout.png')

figure(2)
title('Gaussian Not Fit')
hist(np.ravel(inf_red_10),range(-30,50),density=1)
xlist = np.arange(-30,50,0.01)
ylist = gaussian(xlist,np.mean(inf_red_10),np.std(inf_red_10))
plot(xlist,ylist)
savefig('figure2.png')

figure(3)
title('Comparison of different exposures')
hist(np.ravel(inf_red_10),range(-30,150),density=1,alpha=0.5)
hist(np.ravel(inf_red_20),range(-30,150),density=1,alpha=0.5)
hist(np.ravel(inf_red_60),range(-30,150),density=1,alpha=0.5)
hist(np.ravel(inf_red_120),range(-30,150),density=1,alpha=0.5)

lam1 = 10.7
sigma = 11.12

xlist = np.arange(-25,150,0.01)
#lamda was picked by counts on histogram
poissony = Poisson(xlist,lam1)
poissony[poissony==np.inf] = 0
gaussiany = gaussian(np.arange(-25,25,0.01),0,sigma)
convy = convolve(poissony,gaussiany,mode='same')/95.5
plot(xlist,convy)
text(-35,0.034,'10 seconds',alpha=0.8,fontsize=9)
text(-35,0.032,r'$\lambda$ = '+str(lam1),alpha=0.8,fontsize=9)
text(-35,0.030,r'$\sigma$ = '+str(sigma),alpha=0.8,fontsize=9)

lam2 = 16.76
sigma = 10.9

poissony = Poisson(xlist,lam2)
poissony[poissony==np.inf] = 0
gaussiany = gaussian(np.arange(-30,30,0.01),0,sigma)
convy = convolve(poissony,gaussiany,mode='same')/97.8
plot(xlist,convy)
text(22,0.036,'20 seconds',alpha=0.8,fontsize=9)
text(22,0.034,r'$\lambda$ = '+str(lam2),alpha=0.8,fontsize=9)
text(22,0.032,r'$\sigma$ = '+str(sigma),alpha=0.8,fontsize=9)

lam3 = 48.4
sigma = 10.75

poissony = Poisson(xlist,lam3)
poissony[poissony==np.inf] = 0
gaussiany = gaussian(np.arange(-35,35,0.01),0,sigma)
convy = convolve(poissony,gaussiany,mode='same')/100
plot(xlist,convy)
text(54.5,0.032,'60 seconds',alpha=0.8,fontsize=9)
text(54.5,0.030,r'$\lambda$ = '+str(lam3),alpha=0.8,fontsize=9)
text(54.5,0.028,r'$\sigma$ = '+str(sigma),alpha=0.8,fontsize=9)

lam4 = 98.55
sigma = 11.25

poissony = Poisson(xlist,lam4)
poissony[poissony==np.inf] = 0
gaussiany = gaussian(np.arange(-60,60,0.01),0,sigma)
convy = convolve(poissony,gaussiany,mode='same')/100
plot(xlist,convy)
text(108.3,0.029,'120 seconds',alpha=0.8,fontsize=9)
text(108.3,0.027,r'$\lambda$ = '+str(lam4),alpha=0.8,fontsize=9)
text(108.3,0.025,r'$\sigma$ = '+str(sigma),alpha=0.8,fontsize=9)
savefig('fig3.png')

figure(4)
title('$\lambda$ vs exposure time')
plot([10,20,60,120],[lam1,lam2,lam3,lam4],'o-')
savefig('fig4.png')
show()