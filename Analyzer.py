#! /usr/bin/python
# coding=utf8

from subprocess import call

"""
Created by Han Wang at 2/10/18. 
"""

__author__ = 'Han Wang'

ANALYZER = "scan_build_3.9"

class Analyzer(object):

    def __init__(self, location):
      self.location = location

    def test(self):
      print(call(["cat","Analyzer.py"]))
      print("\n")
      print("hello")

def main():
  a = Analyzer("pwd")
  a.test()

if __name__ == '__main__':
    main()