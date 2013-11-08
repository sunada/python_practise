#coding: UTF-8

import os
import sys

def read_file(filename):
	try:
		f = open(filename)
	except:
		print 'Failed to open the file %s' %s
		exit()

	print "Now the file is :"
	for line in f:
		print line.strip()
	f.close()
	return

def create_file():
	while True:
		filename = raw_input("Please input a filename.\n filename: ")
		if os.path.exists(filename):
			print "%s already exists" % filename
		else:
			break
	contents = []
	print '\nPlease input the content. Input . to stop'
	while True:
		entry = raw_input('>')
		if entry == '.':
			break
		else:
			contents.append(entry)

	f = open(filename, 'w')
	f.writelines(['%s%s' %(line, os.linesep) for line in contents])
	f.close()

	read_file(filename)
	return

def delete_file():
	while True:
		filename = raw_input("Please input a filename.\n filename: ")
		if not os.path.exists(filename):
			print "%s NOT exists" % filename
		else:
			break

	print "The file is: "
	read_file(filename)
	os.remove(filename)
	return

def sort_file_name(lists, big2small = True):
	print sorted(lists.iteritems(), key = lambda d:d[0], reverse = big2small)
	

def sort_file_size(lists, big2small = True):
	return sorted(lists.iteritems(), key = lambda d:d[1], reverse = big2small)

if __name__ == '__main__':
	print "os.name: %s" % os.name
	print "os.getcwd(): %s" % os.getcwd()
	files = os.listdir(os.getcwd())

	lists = {}

	for filename in files:
		lists[filename] = int(os.path.getsize(filename))
		#print " %s (size: %s)" %(filename, lists[filename])
		#print lists[filename]

	print "Sorted by filename: "
	sort_file_name(lists)
	sort_file_name(lists, False)
	
	print "\nSorted by size: "
	print sort_file_size(lists)
	print sort_file_size(lists, False)

	se = raw_input("Input D to delete a file. Input C to create a file. Choice: ")

	while True:
		if se == 'D':
			print "The program will DELETE an exist file."
			delete_file()
			break
		elif se == 'C':
			print "The program will CREATE a new file."
			create_file()
			break
		else:
			print "Illegal input."
			se = raw_input("Please input D (delete) or C (create). Choice: ")

	

	

