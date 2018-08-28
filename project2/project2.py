import sys
sys.path.append("../shared/")
from dataplot import *
import numpy as np


def firstDerivative(ax,ay,bx,by):
	return (by-ay)/(bx-ax)
	
def secondDerivative(x1,y1,x2,y2,x3,y3):
	return 2*(((y3-y2)/((x3-x2)*(x3-x1)))-((y2-y1)/((x2-x1)*(x3-x1))))



BIGHEIGHTSWT_FILE = "../shared/Bigheightswt.dat"
BBHTWT_FILE = "../shared/BBhtwt.dat"

bbHtwt = loadtxt(BBHTWT_FILE)
bigHeights = loadtxt(BIGHEIGHTSWT_FILE)

with open ('project2.out','w') as f:
	print("Mean of BBhtwt.dat is:",mean(bbHtwt[:,1]),file=f)
	print("Std of BBhtwt.dat is:",std(bbHtwt[:,1]),file=f)
	print("Mean of Bigheightswt.dat is:",mean(bigHeights[:,1]),file=f)
	print("Std of Bigheightswt.dat is:",std(bigHeights[:,1]),file=f)

	figure(0)

	plot(bbHtwt[:,0],bbHtwt[:,1],'ro')
	title("bbHtwt weight vs height")
	xlabel("Height")
	ylabel("Weight")
	savefig('bbhtwt-wh.png')

	figure(1)

	plot(bigHeights[:,0],bigHeights[:,1],'ro')
	title("Bigheightswt weight vs height")
	xlabel("Height")
	ylabel("Weight")
	savefig('bigheight-hw.png')

	avg_h_bbhtwt=mean(bbHtwt[:,0])
	avg_w_bbhtwt=mean(bbHtwt[:,1])
	sum_sigmahw_bhtwt = 0
	for i in range(len(bbHtwt[:,0])):
		sum_sigmahw_bhtwt += (bbHtwt[i,0]-avg_h_bbhtwt) * (bbHtwt[i,1]-avg_w_bbhtwt)/len(bbHtwt[:,0])

	print("Correlation error of bhtwt is",sum_sigmahw_bhtwt,file=f)

	avg_h_bigheights=mean([bigHeights[:,0]])
	avg_w_bigheights=mean([bigHeights[:,1]])
	sum_sigmahw_bigheights = 0
	for i in range(len(bigHeights[:,0])):
		sum_sigmahw_bigheights += (bigHeights[i,0]-avg_h_bigheights) * (bigHeights[i,1]-avg_w_bigheights)/len(bigHeights[:,0])

	print("Correlation error of big heights is",sum_sigmahw_bigheights,file=f)

	#pcc-pearson's correlation coefficient
	pcc_bbhtwt = sum_sigmahw_bhtwt / (std(bbHtwt[:,0])*std(bbHtwt[:,1]))
	pcc_bigheights = sum_sigmahw_bigheights / (std(bigHeights[:,0]) * std(bigHeights[:,1]))
	print("Pearson's Correlation Coefficient for bbhtwt is",pcc_bbhtwt,file=f)
	print("Pearson's Correlation Coefficient for bigHeights is",pcc_bigheights,file=f)

	bmi_bbhtwt = 703 * (mean(bbHtwt[:,1]) / (mean(bbHtwt[:,0])**2))
	bmi_bigheight = 703 * (mean(bigHeights[:,1]) / (mean(bigHeights[:,0])**2))
	print("Average bmi values ---------",file=f)
	print("bmi_bbhtwt",bmi_bbhtwt,file=f)
	print("bmi_bigheight",bmi_bigheight,file=f)

	bmi_bbhtwt = zeros(len(bbHtwt[:,0]))
	for i in range (len(bbHtwt[:,0])):
		bmi_bbhtwt[i] = 703 * (bbHtwt[i,1]) / ((bbHtwt[i,0])**2)

	bmi_bigheight = zeros(len(bigHeights[:,0]))
	for i in range (len(bigHeights[:,0])):
		bmi_bigheight[i] = 703 * (bigHeights[i,1]) / (bigHeights[i,0]**2)

	bbHtwt[:,0] = sorted(bbHtwt[:,0])
	bbHtwt[:,1] = sorted(bbHtwt[:,1])
	bmi_bbhtwt = sorted(bmi_bbhtwt)
	bmi_bigheight = sorted(bmi_bigheight)

	figure(2)
	plot(bbHtwt[:,0],bmi_bbhtwt,'ro')
	savefig('bmi.bbbhtwt.png')

	a = (int) (len(bbHtwt[:,0])/2)
	n = 1
	m = 1
	k = 1
	l = 1
	while (bbHtwt[a-n,0] == bbHtwt[a,0]):
		n += 1
	while (bbHtwt[a+m,0] == bbHtwt[a,0]):
		m += 1
	while (bbHtwt[a-k,1] == bbHtwt[a,1]):
		k += 1;
	while (bbHtwt[a+l,1] == bbHtwt[a,1]):
		l += 1

	df_dh = firstDerivative(bbHtwt[a-n,0],bmi_bbhtwt[a-n],bbHtwt[a+m,0],bmi_bbhtwt[a+m])
	df_dw = firstDerivative(bbHtwt[a-k,1],bmi_bbhtwt[a-k],bbHtwt[a+l,1],bmi_bbhtwt[a+l])

	std_1 = std(bbHtwt[:,0])
	std_2 = std(bbHtwt[:,1])

	#print(d2f_dw,std_2)
	print((df_dh**2)* (std_1**2),(df_dw**2) * (std_2**2),2 * df_dh * df_dw * sum_sigmahw_bhtwt)


	sigmahw_bbhtwt = sqrt((df_dh**2) * (std_1**2) + (df_dw**2) * (std_2**2) + 2 * df_dh * df_dw * sum_sigmahw_bhtwt)
	print("bbhtwt std ---------",file=f)
	print("False std",std(bmi_bbhtwt),file=f)
	print("Right std",sigmahw_bbhtwt,file=f)
	

	#Big beight part
	a = (int) (len(bigHeights[:,0])/2)
	n = 1
	m = 1
	k = 1
	l = 1
	while (bigHeights[a-n,0] == bigHeights[a,0]):
		n += 1
	while (bigHeights[a+m,0] == bigHeights[a,0]):
		m += 1
	while (bigHeights[a-k,1] == bigHeights[a,1]):
		k += 1;
	while (bigHeights[a+l,1] == bigHeights[a,1]):
		l += 1

	df_dh = firstDerivative(bigHeights[a-n,0],bmi_bigheight[a-n],bigHeights[a+m,0],bmi_bigheight[a+m])
	df_dw = firstDerivative(bigHeights[a-k,1],bmi_bigheight[a-k],bigHeights[a+l,1],bmi_bigheight[a+l])
	std_1 = std(bigHeights[:,0])
	std_2 = std(bigHeights[:,1])
	print(std_1,std_2,df_dh,df_dw,sum_sigmahw_bigheights)
	sigmahw_bigheight = sqrt((df_dh**2) * (std_1**2) + (df_dw**2) * (std_2**2) + 2 * df_dh * df_dw * sum_sigmahw_bigheights)
	print("Big height std-----",file=f)
	print("False std",std(bmi_bigheight),file=f)
	print("Right std",sigmahw_bigheight,file=f)

#show()