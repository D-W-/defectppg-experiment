#! /usr/bin/python
# coding=utf8

"""
Created by Han Wang at 2/12/18.
3. compare defect list between different versions of projects
"""

__author__ = 'Han Wang'

# FOLDER = "/home/harry/Downloads/task/"

from subprocess import check_output, call
from os.path import join
import Analyzer

class Defect:
    def __init__(self, group, tpe, location, method, line):
        self.group = group
        self.type = tpe
        self.location = location
        self.method = method
        self.line = line
        self.fixed = True

    def __str__(self):
        return "{0}\n".format(
            "::".join((self.location, self.method, self.line, str(self.fixed))))

    def unfix(self):
        self.fixed = False

    def __hash__(self):
        return hash((self.group, self.type, self.location, self.method))

    def __eq__(self, other):
        return (self.group, self.type, self.location, self.method) == (
            other.group, other.type, other.location, other.method)


class Counter(dict):
    def __missing__(self, key):
        return 0


class DefectLabeler:
    def __init__(self):
        pass

    # get list of defects out of defect storage file
    @staticmethod
    def defects_getter(location):
        with open(location) as f:
            defects = f.readlines()
        return [Defect(*defect.strip().split("::")) for defect in defects]

    # label previous defects lists according to current defect list
    def label(self, prev_location, cur_location, out_location, defect_location):
        cur_defects = DefectLabeler.defects_getter(cur_location)
        cur_counter = Counter()
        for defect in cur_defects:
            cur_counter[defect] += 1

        prev_defects = DefectLabeler.defects_getter(prev_location)
        for defect in prev_defects:
            if cur_counter[defect] > 0:
                cur_counter[defect] -= 1
                defect.unfix()

        # defect to absolute path
        for defect in prev_defects :
            defect.location = join(defect_location, defect.location)

        with open(out_location, "w") as f:
            f.writelines([str(defect) for defect in prev_defects])


def main():
    location = Analyzer.LOCATION
    d = "defects.list"
    # out_folders = check_output("ls " + loc + " | grep \"scan\"", shell=True)
    projects_folders = check_output("cd " + location + " && ls -d */", shell=True)
    projects_folders = [join(location, project) for project in projects_folders.strip().split("\n")]
    out_folders = check_output("cd " + location + "&& ls -d */output/*/", shell=True)
    out_folders = [join(location, folder) for folder in out_folders.strip().split("\n")]
    labeler = DefectLabeler()
    for p, c, fd in zip(out_folders[:-1], out_folders[1:], projects_folders):
        print(p, c, fd)
        labeler.label(join(p, d), join(c, d), join(p, "out.list"), fd)

        break


# def test():
#     with open("/home/harry/Downloads/openssl-1.0.0a/output/2018-02-27-212749-38912-1/out.list") as f:
#         defects = f.readlines()
#     defects = [Defect(*defect.strip().split("::")) for defect in defects]
#     for defect in defects:
#         call("cp " + defect.location + ".ll /home/harry/Downloads/task1", shell=True)


if __name__ == "__main__":
    main()
    # test()