from numpy import *
from matplotlib.pyplot import *
def getGaussian(x0,a,min,max,n=500):
	y_axis = []
	x_axis = []
	x_current = min
	step = (max - min)/n
	for i in range(0,n):
		y_axis.append(exp(-((x_current-x0)**2)/(2*(a**2)))/(a*sqrt(2*pi)))
		x_axis.append(x_current)
		x_current += step
	return y_axis, x_axis
	
def histGaussian(dataSet,x0,a,min,max,nn=1000,nbins=10,ndensity=False,ntitle=None):
	if title is not None:
		title(ntitle)
	hist(dataSet,bins=nbins,density=ndensity)
	y,x = getGaussian(x0,a,min,max,n=nn)
	plot(x,y)
