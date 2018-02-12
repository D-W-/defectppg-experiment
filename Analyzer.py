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

    def analyse(self):
        call([ANALYZER, self.location, "-o output"])
        print("analyze phase done.")

    @staticmethod
    def test():
	    # a = call(["cd", "output"])
	    # print(call("ls"))
	    call("cd output && ls", shell=True)
	    # call("ls")
        # print(call(["gcc", "-c "]))
        # print("hello")


def main():
    a = Analyzer("pwd")
    a.test()


if __name__ == '__main__':
    main()