# -*- coding: utf-8 -*

class repoName:
	def __init__ (self,path_file,filed_repo_name):
		self.path_file = path_file
		self.filed_repo_name = filed_repo_name

	def getRepoName(self):
		with open(self.path_file) as f:
			content = f.readlines()

		for line_num in range(len(content)):
			if self.filed_repo_name in content[line_num]:
				repo_name = content[line_num].split("=")[1].strip(" |\"")
		return(repo_name.rstrip(" |\"|\n"))
