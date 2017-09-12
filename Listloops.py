#!/usr/bin/python

the_count = [0, 1, 2, 3, 4, 5]
fruits = ['apples', 'apricots', 'oranges', 'pears']
change = ['quarter', 25, 'dime', 10, 'nickle', 5, 'penny', 1]

for number in the_count:
	print "the count is %d, bwa hahaha" %number

for fruit in fruits:
	print "%s is a fruit" %fruit

for i in change:
	print "I have %r " %i

elements = []

for i in range(0, 6):
	print "I am adding %d to your list" %i 
	elements.append(i)

for i in elements:
	print "the element was %d" %i
