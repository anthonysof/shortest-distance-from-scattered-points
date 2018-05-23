import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg

def main():
	n = 0
	x = []
	x1 = []
	x2 = []
	while n <= 1:
		print "Give me number of points: "
		n = int(raw_input())
		if n <= 1 :
			print "Invalid input, try again"
			if n == 1:
				print "Too easy with only one point, give me more."
		else:
			break;
	points = []
	print "point input format: x y"
	for i in range(n):
		print "Give me point #"+str(i+1)+": "
		point = raw_input()
		point = point.split(" ")
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

	for i in range(n):
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