import requests
import domain_setting
import json
import prettytable
from domain_setting import translate, visible_filelds, domain, api_key

headers = {'PddToken': api_key}

def getAll():
	r = requests.get("https://pddimp.yandex.ru/api2/admin/email/list?"
		"domain={domain}".format(domain=domain), headers=headers)
	result = json.loads(r.content.decode('utf8'))
	table = prettytable.PrettyTable()
	table._set_field_names([translate.get(word) for word in visible_filelds])
	for i in range(0,result['found']):
		table.add_row([result['accounts'][i][k] for k in visible_filelds])
	print(table)

def createUser(login, password):
	print("Создание нового пользователя \n"
			"email: {email}\n"
			"passwd: {password}\n".format(email=login, password=password))
	data = { 'domain' : domain, 'login' : login, 'password' : password }
	r = requests.post("https://pddimp.yandex.ru/api2/admin/email/add", data, headers=headers)
	result = json.loads(r.content.decode('utf8'))
	table = prettytable.PrettyTable()
	table._set_field_names([translate.get(word) for word in dict.keys(result)])
	table.add_row([result[keys] for keys in dict.keys(result)])
	print(table)

def deleteUser(login):
	print("Удаление пользователя \n"
			"email: {email}\n".format(email=login,))
	data = { 'domain' : domain, 'login' : login }
	r = requests.post("https://pddimp.yandex.ru/api2/admin/email/del", data, headers=headers)
	result = json.loads(r.content.decode('utf8'))
	table = prettytable.PrettyTable()
	table._set_field_names([translate.get(word) for word in dict.keys(result)])
	table.add_row([result[keys] for keys in dict.keys(result)])
	print(table)

def modifyUser(**data):
	add_domain = { 'domain' : domain }
	data.update(add_domain)
	print("Модификация пользователя {login}.\n".format(login=data.get('login')))
	r = requests.post("https://pddimp.yandex.ru/api2/admin/email/edit", data, headers=headers)
	result = json.loads(r.content.decode('utf8'))
	table = prettytable.PrettyTable()
	table._set_field_names([translate.get(word) for word in visible_filelds])
	table.add_row([result['account'][k] for k in visible_filelds])
	print(table)
