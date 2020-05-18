# -*- coding: utf-8 -*

#from modules.repoName import repoName
from modules.accessList import accessList
from modules.circleciApi import circleciApi

#repo = repoName("values/values.tfvars","repo_name")
#repoName = repo.getRepoName()
#circleci_api_url = "https://circleci.com/api/v1.1/project/github/reversondias/"+repoName+"/envvar"

access_list = accessList("values/access.list")
#list_a = access_list.getAccess()
#print(list_a)

circleci = circleciApi("circleci_api/data/accessEnv.json",access_list.getAccess())
circleci.setUpCicleCiProject()
circleci.putEnvVarCircleciApi()