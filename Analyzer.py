#! /usr/bin/python
# coding=utf8

"""
Created by Han Wang at 2/10/18. 
1. unzip downloaded projects in folder and analyze them with scan build
"""

from subprocess import call, check_output
from os import path

__author__ = 'Han Wang'

ANALYZER = "scan-build-3.9 "

LOCATION = "//home/harry/testCases/twem"


class Analyzer(object):
    def __init__(self, location):
        self.location = location
        tars = check_output("ls " + location + " | grep \".*.tar.gz\"", shell=True)
        self.tars = tars.strip().split("\n")
        self.projects = [path.join(location, tar.split(".tar.gz")[0]) for tar in self.tars]
        # projects_folders = check_output("cd " + location + " && ls -d */", shell=True)
        # projects_folders = [path.join(location, project) for project in projects_folders.strip().split("\n")]
        # self.projects = projects_folders

    def unzip(self):
        for tar in self.tars:
            call("cd " + self.location + " && tar -zxvf " + tar, shell=True)

    def analyse(self):
        for tar in self.projects:
            call("cd " + tar + " && ./configure ", shell=True)
            call("cd " + tar + " && " + ANALYZER + " -o output make" , shell=True)
        print("analyze phase done.")


def main():
    a = Analyzer(LOCATION)
    a.unzip()
    a.analyse()


if __name__ == '__main__':
    main()