import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
import os
import sys

def main():
	points = []
	x = []
	x1 = []
	x2 = []
	print "Give me name of file: "
	filename = raw_input()
	filestring = ""
	try:
		with open(filename) as openfile:
			statinfo = os.stat(filename)
			while True:
				buf = openfile.read(statinfo.st_size)
				filestring += buf
				if not buf: break		
	except IOError:
		print "File doesnt exist. Try again"
		sys.exit()


	filestring = filestring.replace('(', '').replace('\n',' ').replace('\t',' ')

	filestring = filestring.replace(' ','')
	filestring = filestring.split(")")
	filestring.pop()
	for point in filestring:
		point = point.split(',')
		points.append(point)
		x.append(point[1])
		x1.append(point[0])
		x2.append(1)

	x = np.asarray(x)
	x1 = np.asarray(x1)
	x2 = np.asarray(x2)
	x = x.astype(float)
	x1 = x1.astype(float)
	x2 = x2.astype(float)
	fig = plt.figure()
	ax = plt.axes()

	for i in range(len(points)):
		ax.plot(x1[i],x[i], marker='o', color = 'r')

	print x
	print x1
	print x2

	y1 = x2
	normy1 = linalg.norm(y1)
	v1 = (1/normy1)*y1

	y2 = x1 - np.inner(x1, v1)*v1
	normy2 = linalg.norm(y2)
	v2 = (1/normy2)*y2

	print v1
	print v2

	projection = np.inner(x,v1)*v1 + np.inner(x,v2)*v2
	A = np.array([[x1[0],1],[x1[1],1]])
	B = np.array([projection[0],projection[1]])
	ab = linalg.solve(A, B)
	print ab
	print "The line is y = "+str(ab[0])+"x + "+str(ab[1])
	lns = np.linspace(min(x1),max(x1))
	ax.plot(lns, ab[0]*lns+ab[1] )
	plt.show()


if __name__ == "__main__":
	main()