#!/usr/bin/env python2
#Joseph Daniel Sebacher
#health.py

#The rough draft of the health system for upcoming final project RPG

from sys import stdin, stdout, stderr, argv, exit
import csv

def changeHealth(name, change):
	txt = csv.reader(open('characterconfig.csv', 'rb')) 
	rownum = 0
	save = False
	health = -1
	for row in txt:
		colnum = 0
		for col in row:
			if name == col:
				save = True
			elif save == True:
				health = int(col)
				save = False
			colnum += 1
		rownum += 1

	int(change)
	if health >= 0:
		health += change
		if health < 0:
			health = 0
			return "%s has fallen!" %name
		else:
			return "%s now has %d health" % (name, health)
	else:
		return "Unable to find character"

"""
	infile = csv.writer(open('characterconfig.csv', 'rb'))
	outfile = csv.writer(open('characterconfig.csv', 'wb'))
	rownum = 0
	for row in infile:
		colnum = 0
		for col in row:
			if colnum == 0:
				firstword = col
			else:
				outfile.writerow([firstword, int(col) + 1])
			colnum += 1
		rownum += 1
"""


if __name__ == '__main__':
	from sys import stdin, stderr, stdout, argv
	
	enoughArgs = True
	
	try:
		script, name, change = argv
	except ValueError as e:
		enoughArgs = False

	if enoughArgs == True:
		stdout.write(changeHealth(argv[1], argv[2]))
		stdout.write('\n')
		exit(0)
	elif enoughArgs == False:
		stderr.write("Not enough arguments!\n")
		exit(1)
