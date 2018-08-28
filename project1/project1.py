from dataplot import *
from matplotlib.pyplot import *
from numpy import *
#numpy.loadtxt(fname, dtype=<type 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
#reuturns nth dimension array
rcParams["patch.force_edgecolor"] = True

HOPEHEIGHTS_FILE = "Hopeheights.dat"
BIGHEIGHTSWT_FILE = "Bigheightswt.dat"
BBHTWT_FILE = "BBhtwt.dat"

hopeHeights = loadtxt(HOPEHEIGHTS_FILE)
bbHtwt = loadtxt(BBHTWT_FILE)
bigHeights = loadtxt(BIGHEIGHTSWT_FILE)

std_hopeHeights = std(hopeHeights[:,1])
mean_hopeHeights = mean(hopeHeights[:,1])
std_bbhtwt = std(bbHtwt[:,0])
mean_bbhtwt = mean(bbHtwt[:,0])
std_bigHeights = std(bigHeights[:,0])
mean_bigHeights = mean(bigHeights[:,0])

hopeHeights_male = []
hopeHeights_female = []

for i in range(0,len(hopeHeights)):
	if hopeHeights[i,0].astype(int) == 1: 
		hopeHeights_female.append(hopeHeights[i,1])
	else:
		hopeHeights_male.append(hopeHeights[i,1])

#print(hopeHeights_male)
std_hopeHeights_male = std(hopeHeights_male)
mean_hopeHeights_male = mean(hopeHeights_male)
std_hopeHeights_female = std(hopeHeights_female)
mean_hopeHeights_female = mean(hopeHeights_female)

def _print_both(text,file_name,arg=''):
	print(text,arg)
	print(text,arg,file=file_name)

with open('project1.out','w') as f:
	_print_both("standard deviations --------",f)
	_print_both("hope college height:",f,std_hopeHeights)
	_print_both("hope college height male:",f,std_hopeHeights_male)
	_print_both("hope college height female",f,std_hopeHeights_female)
	_print_both("professional baseball players height:",f,std_bbhtwt)
	_print_both("adolescents height:",f,std_bigHeights)
	_print_both("mean values --------",f)
	_print_both("hope college height:",f,mean_hopeHeights)
	_print_both("hope college height male:",f,mean_hopeHeights_male)
	_print_both("hope college height female",f,mean_hopeHeights_female)
	_print_both("professional baseball players height:",f,mean_bbhtwt)
	_print_both("adolescents height:",f,mean_bigHeights)

hopeHeights_y, hopeHeights_x = getGaussian(mean_hopeHeights,std_hopeHeights,min(hopeHeights[:,1]),max(hopeHeights[:,1]))
hopeHeights_male_y, hopeHeights_male_x = getGaussian(mean_hopeHeights_male,std_hopeHeights_male,min(hopeHeights_male),max(hopeHeights_male))
hopeHeights_female_y, hopeHeights_female_x = getGaussian(mean_hopeHeights_female,std_hopeHeights_female,min(hopeHeights_female),max(hopeHeights_female))
bbhtwt_y, bbhtwt_x = getGaussian(mean_bbhtwt,std_bbhtwt,min(bbHtwt[:,0]),max(bbHtwt[:,0]))
bigHeights_y, bigHeights_x = getGaussian(mean_bigHeights,std_bigHeights,min(bigHeights[:,0]),max(bigHeights[:,0]))


figure(1)
histGaussian(hopeHeights[:,1],mean_hopeHeights,std_hopeHeights,min(hopeHeights[:,1]),max(hopeHeights[:,1]),\
	ndensity=True,ntitle="Height for Hope College")
figure(2)
histGaussian(hopeHeights_male,mean_hopeHeights_male,std_hopeHeights_male,min(hopeHeights_male),max(hopeHeights_male),\
	ndensity=True,ntitle="Height for Hope College Male")
figure(3)
histGaussian(hopeHeights_female,mean_hopeHeights_female,std_hopeHeights_female,min(hopeHeights_female),max(hopeHeights_female),\
	ndensity=True,ntitle="Height for Hope College Female")
figure(4)
histGaussian(bbHtwt[:,0],mean_bbhtwt,std_bbhtwt,min(bbHtwt[:,0]),max(bbHtwt[:,0]),nbins=15,\
	ndensity=True,ntitle="Height for professional baseball players height")
figure(5)
histGaussian(bigHeights[:,0],mean_bigHeights,std_bigHeights,min(bigHeights[:,0]),max(bigHeights[:,0]),nbins=30,\
	ndensity=True,ntitle="Height for 25000 adolescents")
show()
