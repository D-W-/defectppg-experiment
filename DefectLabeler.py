#! /usr/bin/python
# coding=utf8

"""
Created by Han Wang at 2/12/18. 
"""

__author__ = 'Han Wang'


class Defect:
	def __init__(self, group, tpe, location, method):
		self.group = group
		self.type = tpe
		self.location = location
		self.method = method

	def __hash__(self):
		return hash((self.group, self.type, self.location, self.method))

	def __eq__(self, other):
		return (self.group, self.type, self.location, self.method) == (
		other.group, other.type, other.location, other.method)

