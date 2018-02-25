#! /usr/bin/python
# coding=utf8

"""
Created by Han Wang at 2/12/18.
3. compare defect list between different versions of projects
"""

__author__ = 'Han Wang'

from subprocess import check_output
from os.path import join


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
    def label(self, prev_location, cur_location, out_location):
        cur_defects = DefectLabeler.defects_getter(cur_location)
        cur_counter = Counter()
        for defect in cur_defects:
            cur_counter[defect] += 1

        prev_defects = DefectLabeler.defects_getter(prev_location)
        for defect in prev_defects:
            if cur_counter[defect] > 0:
                cur_counter[defect] -= 1
                defect.unfix()

        with open(out_location, "w") as f:
            f.writelines([str(defect) for defect in prev_defects])


def main():
    loc = "output"
    d = "defects.list"
    out_folders = check_output("ls " + loc + " | grep \"scan\"", shell=True)
    out_folders = [join(loc, folder) for folder in out_folders.strip().split("\n")]
    labeler = DefectLabeler()
    for p, c in zip(out_folders[:-1], out_folders[1:]):
        print(p, c)
        labeler.label(join(p, d), join(c, d), join(p, "out.list"))

if __name__ == "__main__":
    main()
