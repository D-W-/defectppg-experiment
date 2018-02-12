#! /usr/bin/python
# coding=utf8

"""
Created by Han Wang at 2/11/18. 
"""

from bs4 import BeautifulSoup
import os

__author__ = 'Han Wang'

INPUT = 'index.html'
OUTPUT = 'defects.list'


def toText(item):
	return item.text

class OutputParser:
	def __init__(self, location):
		# type: (object) -> object
		self.location = location
		with open(os.path.join(location, INPUT)) as f:
			self.content = f.read()
		# print self.content

	def parse(self):
		# find table contents in html
		soup = BeautifulSoup(self.content, 'html.parser')
		table = soup.findAll('tbody')[0]
		data = [map(toText, tr.findAll('td')) for tr in table.findAll('tr')]
		data = ["::".join(line[0:5]) + '\n' for line in data]
		# store parsed table data into file
		with open(os.path.join(self.location, OUTPUT), 'w') as f:
			f.writelines(data)


		
		
def main():
	parser = OutputParser("output")
	parser.parse()
	

if __name__ == '__main__':
	main()
