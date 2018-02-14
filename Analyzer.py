#! /usr/bin/python
# coding=utf8

from subprocess import call, check_output
from os import path

"""
Created by Han Wang at 2/10/18. 
"""

__author__ = 'Han Wang'

ANALYZER = "scan-build-3.9 "

LOCATION = "/home/harry/Downloads"


class Analyzer(object):
	def __init__(self, location):
		self.location = location
		tars = check_output("ls " + location + " | grep \".*.tar.gz\"", shell=True)
		self.tars = tars.strip().split("\n")
		self.projects = [path.join(location, tar.split(".tar.gz")[0]) for tar in self.tars]

	def unzip(self):
		for tar in self.tars:
			call("cd " + self.location + " && tar -zxvf " + tar, shell=True)

	def analyse(self):
		for tar in self.projects:
			call("cd " + tar + " && ./config no-asm", shell=True)
			call("cd " + tar + " && " + ANALYZER + " -o output make" , shell=True)
		print("analyze phase done.")


def main():
	a = Analyzer(LOCATION)
	# a.unzip()
	a.analyse()


if __name__ == '__main__':
	main()