from numpy import *
from matplotlib.pyplot import *
def getGaussian(x0,a,min,max,n=500,amplitude=1):
	y = []
	x = []
	xt = min
	step = (max - min)/n
	for i in range(0,n):
		y.append(amplitude*exp(-((xt-x0)**2)/(2*(a**2)))/(a*sqrt(2*pi)))
		x.append(xt)
		xt += step
	return y,x
	
def histGaussian(dataSet,x0,a,min,max,nn=1000,nbins=10,ndensity=False,ntitle=None,namplitude=1,gaus=True):
	if title is not None:
		title(ntitle)
	if(ndensity == True and namplitude != 1):
		print("\nIncorrect input, having normalized histgram but non-normalized gaussian distribution. \nDataplot.py Line 18\n")
	hist(dataSet,bins=nbins,density=ndensity)
	if(gaus == True):
		y,x = getGaussian(x0,a,min,max,n=nn,amplitude=namplitude)
		plot(x,y)

