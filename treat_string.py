#!/bin/python

#input www.xxx.com/abc/index.html
#output com#xxx#www*index.html

def treat_string(str):
	arr = str.split('/')
	arr0 = arr[0].split('.')
	arr0_rev = [x for x in arr0[::-1]]
	dom_rev = '#'.join(arr0_rev)
	new_str = dom_rev + '*' +'/'.join(arr[1:])
	print new_str


if __name__ == '__main__':
	str = 'www.xxx.com/abc/index.html'
	treat_string(str)
