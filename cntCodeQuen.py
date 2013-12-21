import os
import sys

#roughly count code lines in a dir
def cntLines(dirName, cnt = 0):
	files = os.listdir(dirName)
	for file in files:
		filename = dirName + '/' + file
		print filename
		if os.path.isdir(filename):
			cnt += cntLines(filename, cnt)
		else:
			lines = open(filename)
			for line in lines:
				cnt += 1
			#print 'cnt = ' + str(cnt)
	return cnt

if __name__ == '__main__':
	dirName = sys.argv[1]
	res = cntLines(dirName)
	print res


