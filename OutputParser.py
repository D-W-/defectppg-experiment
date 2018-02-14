#! /usr/bin/python
# coding=utf8

"""
Created by Han Wang at 2/11/18. 
"""

from bs4 import BeautifulSoup
import os
from subprocess import check_output

__author__ = 'Han Wang'

INPUT = 'index.html'
OUTPUT = 'defects.list'


def toText(item):
	return item.text

class OutputParser:
	def __init__(self):
		pass

	def parse(self, location):
		with open(os.path.join(location, INPUT)) as f:
			content = f.read()
		# find table contents in html
		soup = BeautifulSoup(content, 'html.parser')
		table = soup.findAll('tbody')[0]
		data = [map(toText, tr.findAll('td')) for tr in table.findAll('tr')]
		data = ["::".join(line[0:5]) + '\n' for line in data]
		# store parsed table data into file
		with open(os.path.join(location, OUTPUT), 'w') as f:
			f.writelines(data)

		
def main():
	location = "output"
	out_folders = check_output("ls " + location + " | grep \"scan\"", shell=True)
	out_folders = out_folders.strip().split("\n")

	parser = OutputParser()
	for folder in out_folders:
		parser.parse(os.path.join(location, folder))
	

if __name__ == '__main__':
	main()
