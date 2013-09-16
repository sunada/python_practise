#!/usr/bin/python

import sys
import random
import time

def bubble(origin):
    cnt = len(origin)
    while cnt:
        for i in range(cnt -1):
            if origin[i] < origin[i + 1]:
                origin[i], origin[i + 1] = origin[i + 1], origin[i]
        cnt -= 1

    return origin

def insertion(origin):
    cnt = len(origin)
    for i in range(1, cnt):
        key = origin[i]
        j = i - 1
        while j >= 0 and key > origin[j]:
            origin[j + 1] = origin[j]
            j -= 1
        origin[j + 1] = key
    return origin
       
def selection(origin):
    cnt = len(origin)
    flag = 0
 
    while flag < cnt:
        mx = origin[flag]
        mx_i = flag
        for i in range(flag+1, cnt):
            if origin[i] > mx:
                mx_i = i
                mx = origin[i]
        origin[flag], origin[mx_i] = origin[mx_i], origin[flag]
        flag += 1
    return origin

def quick(origin, left, right):
    if right <= left:
        return
    move = 'left'
    base = origin[right]
    flag_left = left
    flag_right = right

    while left < right:
        if origin[right] > origin[left]:
            origin[right], origin[left] = origin[left], origin[right]
            move = 'right' if origin[left] == base else 'left'
            
        if move == 'left':
            left += 1
        else:
            right -= 1
    quick(origin, flag_left, right - 1)
    quick(origin, right, flag_right)
    
def quick2(origin, left, right):
    if left >= right:
        return origin

    lp = left
    rp = right
    key = origin[right]
    
    while True:
        while origin[lp] >= key and lp < rp:
            lp += 1
        while origin[rp] <= key and lp < rp:
            rp -= 1
        origin[lp], origin[rp] = origin[rp], origin[lp]
        if lp >= rp:
            break
    origin[rp], origin[right] = origin[right], origin[rp]

    quick2(origin, left, rp - 1);
    quick2(origin, rp + 1, right);
    
    return origin
    

def shell(origin, gap):
    while gap > 0:
        for i in range(len(origin)):
            key = origin[i]
            j = i - gap
            while j >= 0 and origin[j] < key:
                origin[j + gap] = origin[j]
                j -= gap
            origin[j + gap] = key
        gap = gap/2
    return origin

def heap(origin):
    #build a heap by origin[i:] 
    def build_heap(origin, i):
        lchild = origin[2 * i + 1] if 2 * i + 1 < len(origin) else origin[i]
        rchild = origin[2 * i + 2] if 2 * i + 2 < len(origin) else origin[i]
        flag = i
        if origin[flag] < lchild:
            flag = 2 * i + 1
        if origin[flag] < rchild:
            flag = 2 * i + 2
        if flag != i:
            origin[flag], origin[i] = origin[i], origin[flag]
            build_heap(origin, flag)

    #adjust
    sort = []
    def adjust(origin, sort):
        cnt = len(origin)
        while cnt:
            sort.append(origin[0])
            origin[0], origin[cnt - 1] = origin[cnt - 1], origin[0]
            del(origin[cnt - 1])
            cnt = len(origin)
            for i in range(cnt / 2 - 1, -1, -1):
                build_heap(origin, i)

    #build a heap by origin[:]
    tmp = len(origin) / 2 - 1
    for i in range(tmp, -1, -1):
        build_heap(origin, i)
    
    #heap sorting
    sort = []
    adjust(origin, sort)
    return sort 

def counting(origin):
    cnt = len(origin)
    count = [0] * cnt
    for i in range(cnt):
        for j in range(cnt):
            if origin[i] < origin[j]:
                count[i] += 1

    sort = [-1] * cnt
    for i in range(cnt):
        if sort[count[i]] == -1:
            sort[count[i]] = origin[i]
        else:
            sort[count[i] + 1] = origin[i]
    return sort

def radix(origin):
    radix = 10
    base = 1
    mx = max(origin)

    while mx%radix/base > 0:
        bullet = [ [] for x in range(10)]
        for x in origin:
            index = x % radix / base
            bullet[index].append(x)

        origin = []
        for i in bullet[::-1]:
            origin.extend(i)
        
        radix *= 10
        base *= 10
    
    return origin

def merge_sort(arr):
    def merge(arr1, arr2):
        i = 0
        j = 0
        merge_arr = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                merge_arr.append(arr1[i])
                i += 1
            else:
                merge_arr.append(arr2[j])
                j += 1
        if i == len(arr1):
            merge_arr.extend(arr2[j:])
        else:
            merge_arr.extend(arr1[i:])
        return merge_arr
        
    length = len(arr)
    if length == 1:
        return arr

    tmp_a = merge_sort(arr[0:length/2])
    tmp_b = merge_sort(arr[length/2:])
    return merge(tmp_a, tmp_b)

if __name__ == '__main__':
    origin = [6, 6, 7, 5, 3, 2, 4, 1, 8, 9, 0]
    print 'before sort:           ', origin
    sort = bubble(origin[:])
    print 'after sort (bubble):   ', sort

    sort = insertion(origin[:])
    print 'after sort (insertion):', sort

    sort = shell(origin[:], 5)
    print 'after sort (shell):    ', sort
    
    sort = selection(origin[:])
    print 'after sort (selection):', sort

    sort = origin[:]
    quick(sort, 0, len(sort)-1)
    print 'after sort (quick):    ', sort
    
    sort = origin[:]
    quick2(sort, 0, len(sort)-1)
    print 'after sort (quick2):   ', sort

    sort = heap(origin[:])
    print 'after sort (heap):     ', sort

    sort = counting(origin[:])
    print 'after sort (counting): ', sort

    lenth = 30
    arr = []
    #set the maximum depth as 100000
    sys.setrecursionlimit(100000)
    for i in range(lenth):
        arr.append(random.randint(0, 1000))

    print 'before sort, arr: ', arr
    start = time.time()
    sort = quick2(arr[:], 0, len(arr)-1)
    cost = time.time() - start
    print 'cost %d seconds' %cost
    print 'after sort (quick2):  ', sort
    
    start = time.time()
    sort = radix(arr[:])
    cost = time.time() - start
    print 'cost %d seconds' %cost
    print 'after sort (radix):  ', sort

    start = time.time()
    sort = merge_sort(arr[:])
    cost = time.time() - start
    print 'cost %d seconds' %cost
    print 'after sort (merge):  ', sort
