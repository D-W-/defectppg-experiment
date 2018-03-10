#! /usr/bin/python
# coding=utf8

"""
Created by Han Wang at 2/27/18.
4. build-capture all projects and extract .i files into a folder to analyze
"""

import Analyzer
import os
from subprocess import call, check_output


__author__ = 'Han Wang'

BUILD = "/home/harry/code/myProjects/Build-capture/out/artifacts/Build_capture_jar/"


class BuildCaptor:
    def __init__(self):
        pass

    @staticmethod
    def build_capture(folder):
        call("cd " + BUILD + " && java -jar Build-capture.jar " + folder + " make ", shell=True)

    @staticmethod
    def move2task(folder):
        call("cd " + folder + " && mkdir task", shell=True)
        call("cd " + folder + " && cp line*/*.i task", shell=True)


def main():
    location = Analyzer.LOCATION
    out_folders = check_output("cd " + location + " && ls -d */", shell=True)
    out_folders = [os.path.join(location, folder) for folder in out_folders.strip().split("\n")]
    for folder in out_folders:
        # folder += "/example"
        call("cd " + folder + " && make clean && rm .process_makefile -rf", shell=True)
        BuildCaptor.build_capture(folder)
        BuildCaptor.move2task(os.path.join(folder, ".process_makefile"))
        break


if __name__ == '__main__':
    main()