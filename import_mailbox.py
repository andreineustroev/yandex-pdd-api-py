import requests
import domain_setting
import json
import prettytable
from domain_setting import translate, visible_filelds, domain, api_key, mailMethod, mailServer, mailPort, mailPort, mailSsl

headers = {'PddToken': api_key}

def checkConnect():
	r = requests.get("https://pddimp.yandex.ru/api2/admin/import/check_settings?"
					"domain={domain}&method={mailMethod}&server={mailServer}&"
					"port={mailPort}&ssl={mailSsl}".format(domain=domain,
															mailMethod=mailMethod,
															mailServer=mailServer,
															mailPort=mailPort,
															mailSsl=mailSsl ), headers=headers)
	result = json.loads(r.content.decode('utf8'))
	print(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))


def importMailbox(extLogin, extPasswd):
	data = { 
		'domain'     : domain,  
		'method'     : mailMethod,
		'server'     : mailServer,
		'port'       : mailPort,
		'ssl'        : mailSsl,
		'ext-login'	 : extLogin,
		'ext-passwd' : extPasswd,
	}

	r = requests.post("https://pddimp.yandex.ru/api2/admin/import/start_one_import", data, headers=headers)
	result = json.loads(r.content.decode('utf8'))
	print(json.dumps(result, sort_keys=True, indent=4, separators=(',',': ')))

def importStatus():
	r = requests.get("https://pddimp.yandex.ru/api2/admin/import/check_imports?domain={domain}".format(domain=domain), 
																								headers=headers)
	result = json.loads(r.content.decode('utf8'))
	print(json.dumps(result, sort_keys=True, indent=4, separators=(',',': ')))

def importAbort():
	r = requests.post("https://pddimp.yandex.ru/api2/admin/import/stop_all_imports?domain={domain}".format(domain=domain), 
																								headers=headers)
	result = json.loads(r.content.decode('utf8'))
	print(json.dumps(result, sort_keys=True, indent=4, separators=(',',': ')))
