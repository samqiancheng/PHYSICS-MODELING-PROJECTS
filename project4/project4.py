import numpy as np
from matplotlib.pyplot import *
import atexit

table =""



def printDash():
	global table
	table += '---------------------------------------------' + '\n'

def writeLog(string,n1,n2):
	global table
	table += '|'+'{:^13}'.format(string)+'|'+'{:14.4E}'.format(n1)+'|'+'{:14.4E}'.format(n2)+'|' + '\n'
	printDash()

def maketable():
	global table
	print(table)

def em_std(v,i,r):
	a = 0.15
	n = 130
	mu = 1.26 * (10 **(-6))
	dv = (125/32) * (a / (r * i * mu * n)) ** 2
	dr = -2 * (125 * v / 32) * ((a/(i * mu * n))**2) * r ** (-3)
	di = -2 * (125 * v / 32) * ((a / (r * mu * n))**2) * i ** (-3)
	_v = 10 **_lastdigit(v)
	_i = 10 ** _lastdigit(i)
	
	return (((dv * _v)**2 + (dr * (0.5 / 1000))**2 + (di * _i)**2) ** (0.5))

def _lastdigit(n):
	tmp = str(n)
	index = tmp.find('.')
	if (index == -1):
		return int(0)
	else:
		return -int(len(tmp) - index - 1)
#print table header

atexit.register(maketable)

printDash()
table += '|'+'{:^13}'.format('NAME')+'|'+'{:^14}'.format('MEAN')+'|'+'{:^14}'.format('STD')+'|' + '\n'
printDash()

# Volts Amps CM
em1 = np.loadtxt('em1.dat')
em2 = np.loadtxt('em2.dat')
#convert from cm to m
em1[:,2] = [i/100 for i in em1[:,2]]
em2[:,2] = [i/100 for i in em2[:,2]]

#adding e/m to forth column em[:,3]
e_m_1 = (125 * em1[:,0] / 32) * (0.15 / (1.26 * 10 ** (-6) * 130 * em1[:,1] * em1[:,2])) ** 2
print('e/m for em1')
print(e_m_1)
e_m_1 = np.vstack(e_m_1)
em1 = np.append(em1,e_m_1,axis=1)
e_m_2 = (125 * em2[:,0] / 32) * (0.15 / (1.26 * 10 ** (-6) * 130 * em2[:,1] * em2[:,2])) ** 2
print('e/m for em2')
print(e_m_2)
e_m_2 = np.vstack(e_m_2)
em2 = np.append(em2,e_m_2,axis=1)

#print(em1)
writeLog('em1',np.mean(em1[:,3]),np.std(em1[:,3]))
writeLog('em2',np.mean(em2[:,3]),np.std(em2[:,3]))

figure(1)
hist(em1[:,3],bins='auto')
savefig('em1.png')
figure(2)
hist(em2[:,3],bins='auto')
savefig('em2.png')
em1stdlist = em_std(em1[:,0],em1[:,1],em1[:,2])
em2stdlist = em_std(em2[:,0],em2[:,1],em2[:,2])


print(em1stdlist)
print(em2stdlist)

figure(3)
plot(em1[:,0],em1[:,3],'ro')
title('em1 vs V')
savefig('emvsv1.png')
figure(4)
plot(em2[:,0],em2[:,3],'ro')
title('em2 vs V')
savefig('emvsv2.png')

std_mix = np.mean((em1[:,0]-np.mean(em1[:,0]))*(em1[:,3]-np.mean(em1[:,3])))/len(em1[:,0])
pcc_em1 = std_mix / (np.std(em1[:,0]) * np.std(em1[:,3]))
print(pcc_em1)

std_mix = np.mean((em2[:,0]-np.mean(em2[:,0]))*(em2[:,3]-np.mean(em2[:,3])))/len(em2[:,0])
pcc_em2 = std_mix / (np.std(em2[:,0]) * np.std(em2[:,3]))
print(pcc_em2)
#show()
