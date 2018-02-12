#! /usr/bin/python
# coding=utf8

"""
Created by Han Wang at 2/12/18. 
"""

__author__ = 'Han Wang'

# import OutputParser


class Defect:
	def __init__(self, group, tpe, location, method, line):
		self.group = group
		self.type = tpe
		self.location = location
		self.method = method
		self.line = line
		self.fixed = True

	def __str__(self):
		return "::".join((self.location, self.method, self.line, str(self.fixed))) + "\n"

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
	labeler = DefectLabeler()
	labeler.label("output/defects1.list", "output/defects2.list", "output/out.list")
	d = Defect("1","2","3","4","5")
	print(str(d))


if __name__ == "__main__":
    main()