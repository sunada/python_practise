import sys

FLAG = -1

def is_num(a):
	try:
		res = float(a)
		return res
	except:
		return FLAG

def is_triangle(a, b, c):
	a1 = is_num(a)
	b1 = is_num(b)
	c1 = is_num(c)
	if a1 == FLAG or b1 == FLAG or c1 == FLAG:
		print "(%s, %s, %s) should all be numbers." %(a, b, c)
		return
	if a1 <= 0 or b1 <= 0 or c1 <= 0:
		print "(%s, %s, %s) should all be bigger than 0." %(a1, b1, c1)
		return
	arr = [a1, b1, c1]
	arr.sort()
	if arr[0] + arr[1] <= arr[2]:
		print "(%s, %s, %s) can not build a triangle (because %s + %s <= %s)"\
		 %(arr[0], arr[1], arr[2], arr[0], arr[1], arr[2])
		return
	if arr[0] == arr[2]:
		print "(%s, %s, %s) can build an equilateral triangle" %(arr[0], arr[1], arr[2])
	elif arr[0] == arr[1] or arr[1] == arr[2]:
		print "(%s, %s, %s) can build an isosceles triangle" %(arr[0], arr[1], arr[2])
	else:
		print "(%s, %s, %s) can build a common triangle." %(arr[0], arr[1], arr[2])


if __name__ == '__main__':
	filename = sys.argv[1]
	lines = open(filename)
	for line in lines:
		line = line.strip()
		arr = line.split(' ')
		is_triangle(arr[0], arr[1], arr[2])