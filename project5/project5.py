import numpy as np
from matplotlib.pyplot import *
import operator
#failed to work
def _L_(const,sigma_v,sigma_i,v_i):
	_sum_=1
	for i in range(len(sigma_i)):
		_temp_ = (np.exp(-v_i[i]**2/(2*(sigma_v**2+sigma_i[i]**2))) / (np.sqrt(sigma_v**2+sigma_i[i]**2)))
		_sum_*=const*_temp_
		#print(_temp_)
	return _sum_

#function to calculate ln(likelihood)
def _ln_L_(sigma_v,sigma_i,v_i,const=0):
	_sum_ = 0
	for i in range(len(sigma_i)):
		_sum_ += ((-0.5 * np.log(sigma_i[i]**2+sigma_v**2)) - (v_i[i]**2)/(2*(sigma_v**2+sigma_i[i]**2)))
	return _sum_+const

def gaussian(x,x0,a):   # this defines a normalized gaussian function
    return( np.exp(-(x-x0)**2/(2.0*a**2))/np.sqrt(2.0*np.pi*a**2) )   # note that the math functions and pi are contained in the numpy library




#set x-range
xlist = np.arange(-1000,1000,1)
#v_i,sigma_i
galvel = np.loadtxt('galvel.dat')
gprvel = np.loadtxt('gprvel.dat')

print(np.mean(galvel[:,0]))
print(np.mean(gprvel[:,0]))

print(np.std([500.14-328.59]))
quit()

#_L_list contains ln(likelihood) using xlist
_L_list_ = _ln_L_(xlist,galvel[:,1],galvel[:,0])
plot(xlist,_L_list_)
figure()
_L_list_ = _ln_L_(xlist,gprvel[:,1],gprvel[:,0])
plot(xlist,_L_list_)
C=-np.max(_L_list_)
print(C)

xlist = np.arange(420,570,0.01)

plotlist = np.exp(_ln_L_(xlist,galvel[:,1],galvel[:,0],const=C))
#print(plotlist)
figure()
plot(xlist,plotlist)
index,value = max(enumerate(plotlist),key=operator.itemgetter(1))
print(index)
gaussianlist = gaussian(xlist[index],xlist,18)
percent = np.max(plotlist)/np.max(gaussianlist)
gaussianlist = [i*percent for i in gaussianlist]
print('#',len(galvel[:,0]),xlist[index])
plot(xlist,gaussianlist)

xlist = np.arange(250,400,0.01)
C=-np.max(_ln_L_(xlist,gprvel[:,1],gprvel[:,0]))
plotlist = np.exp(_ln_L_(xlist,gprvel[:,1],gprvel[:,0],const=C))
figure()
plot(xlist,plotlist)
index,value = max(enumerate(plotlist),key=operator.itemgetter(1))
gaussianlist = gaussian(xlist[index],xlist,19.8)
percent = np.max(plotlist)/np.max(gaussianlist)
gaussianlist = [i*percent for i in gaussianlist]
plot(xlist,gaussianlist)
print('#',len(gprvel[:,0]),xlist[index])

#hist for first set
figure()
histlist=[]
for i in range(len(galvel[:,0])):
	histlist.append(galvel[i,0]/np.sqrt(18**2+galvel[i,1]**2))
hist(histlist,bins=15,density=1)
x=np.arange(-4,6,0.1)
plot(x,gaussian(0,x,1))

figure()
histlist=[]
for i in range(len(gprvel[:,0])):
	histlist.append(gprvel[i,0]/np.sqrt(19.8**2+gprvel[i,1]**2))
hist(histlist,bins=15,density=1)
x=np.arange(-4,6,0.1)
plot(x,gaussian(0,x,1))
show()
