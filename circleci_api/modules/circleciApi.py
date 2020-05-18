# -*- coding: utf-8 -*

import json
import requests
import os
from modules.repoName import repoName

class circleciApi:
	def __init__ (self,path_json_file,access_list):
		self.access_list = access_list
		self.path_json_file = path_json_file
		#self.circleci_api_url = circleci_api_url

		#Recupera o nome do projeto no arquivo values/values.tfvars.
		self.repo = repoName("values/values.tfvars","repo_name")
		
		#Recupera o Token de acesso ao CircleCI. É uma env var.
		circleci_token = os.getenv("CIRCLECI_TOKEN")
		self.params={"circle-token":circleci_token} #Monta o parâmetro de autenticação via token do CircleCI

		#Recupera o nome do usuário que pode criar as variáveis no CircleCI
		self.circleci_user = os.getenv("CIRCLECI_USER") ### Arrumar a condição se não tiver o var env

	def getAccessEnv(self):
		#Baseado na lista que recebe da leitura do arquivo, carrega as variáveis de ambiente do JSON
		env_list = []

		with open(self.path_json_file) as json_file:
			json_content = json.load(json_file)

		for key in self.access_list:
			for env in json_content[0][key]:
				env_list.append(env)
		
		#Retorna uma lista de todos os nomes de variáveis de ambiente do JSON
		return(env_list)

	def getEnvVar(self):
		#Baseado na Lista de nomes de váriais recebidas monta um dic com o nome e o valor.

		env_list = self.getAccessEnv()
		env_var_dict = {}

		for env in env_list:
			env_value = os.getenv(env)
			env_var_dict[env] = env_value

		#Retorna um dic com nome e valor das variáveis de ambiente.
		return(env_var_dict)


	def putEnvVarCircleciApi(self):
		#Realiza o POST no projeto em questão no CircleCI.

		#Recebe o dic com os nomes e valores das variáveis a serem criadas.
		env_var_dict = 	self.getEnvVar()

		#Monta a URL de acesso.
		circleci_api_url = "https://circleci.com/api/v1.1/project/github/"+self.circleci_user+"/"+self.repo.getRepoName()+"/envvar"
		
		#Laço que cria o payload para criação das variáveis no projeto. Ele só envia de nome e valor, se colocar mais ele aceita só o último.
		for key in env_var_dict:
			data = {"name": key, "value": env_var_dict[key]}
			response = requests.post(circleci_api_url,params=self.params,data=data)
			if response.status_code == 201 :
				print("[OK] A variável foi criada com sucesso!")
				print(response.text)
			else:
				print("[ERROR] Houve algum problema na criação da variável: "+key)

	def setUpCicleCiProject(self):
		#Realiza o set up do projeto no circleCI

		circleci_api_url = "https://circleci.com/api/v1.1/project/github/"+self.circleci_user+"/"+self.repo.getRepoName()+"/follow"
		response = requests.post(circleci_api_url,params=self.params)
		if response.status_code == 200:
			print("[OK] O setup do repositório"+self.repo.getRepoName()+" foi configurado com sucesso!")
			print(response.text)
		else:
			print("[ERROR] Houve algum problema na configuração do setup do repositório: "+self.repo.getRepoName())


