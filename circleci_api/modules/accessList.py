# -*- coding: utf-8 -*

class accessList:
	def __init__ (self,path_file):
		self.path_file = path_file
		
	def getAccess(self):

		access_list = []

		with open(self.path_file) as f:
			content = f.readlines()

		for line_num in range(len(content)):
			if "true" in content[line_num]:
				access_list.append(content[line_num].split("=")[0].strip(" ").rstrip(" |\n"))
		return(access_list)
