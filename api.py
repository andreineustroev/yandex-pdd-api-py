#!/usr/bin/python3

import sys
import get
import import_mailbox

try:
	sys.argv[1]
except IndexError as e:
	print("Введите действие. Возможные значения:\n"
		"get all - получить все ящики\n"
		"create - создать ящик\n"
		"delete - удалить ящик\n"
		"modifypass - изменить пароль\n"
		"modifyname - изменить имя\n"
		"modifysex - изменить пол\n"
		"modifyen - включить/выключить акаунт\n"
		"\n"
		"Импорт ящиков:\n"
		"checkconnect - проверка возможности импорта\n"
		"importmailbox - импорт одного ящика\n"
		"importstatus - статус импорта\n")
	action = "none"
else:
	action = sys.argv[1]

if action == "get":
	if sys.argv[2] == 'all':
		get.getAll()

if action == "create":
	try:
		sys.argv[3]
	except Exception as e:
		print("Не хватает аргументов, синтаксис \n"
				"api.py create login password")
	else:
		get.createUser(sys.argv[2], sys.argv[3])

if action == "delete":
	try:
		sys.argv[2]
	except Exception as e:
		print("Не хватает аргументов, синтаксис \n"
				"api.py delete login")
	else:
		get.deleteUser(sys.argv[2])

if action == "modifypass":
	try:
		sys.argv[3]
	except Exception as e:
		print("Не хватает аргументов, синтаксис \n"
			"api.py modifypass login newpass")
	else:
		get.modifyUser(login=sys.argv[2], password=sys.argv[3])

if action == "modifyname":
	try:
		sys.argv[4]
	except Exception as e:
		print("Не хватает аргументов, синтаксис \n"
			"api.py modifypass login newname newfname")
	else:
		get.modifyUser(login=sys.argv[2], iname=sys.argv[3], fname=sys.argv[4])

#Ну мало ли
if action == "modifysex":
	try:
		sys.argv[3]
	except Exception as e:
		print("Не хватает аргументов, синтаксис \n"
			"api.py modifypass login newsex[1/2]\n"
			"1 - male, 2 - female\n")
	else:
		get.modifyUser(login=sys.argv[2], sex=sys.argv[3])

if action == "modifyen":
	try:
		sys.argv[3]
	except Exception as e:
		print("Не хватает аргументов, синтаксис \n"
			"api.py modifypass login [yes/no]")
	else:
		get.modifyUser(login=sys.argv[2], enabled=sys.argv[3])

if action == "checkconnect":
	import_mailbox.checkConnect()

if action == "importmailbox":
	try:
		sys.argv[3]
	except Exception as e:
		print("Не хватает аргументов, синтаксис \n"
			"api.py login password")
	else:
		import_mailbox.importMailbox(extLogin=sys.argv[2], extPasswd=sys.argv[3])

if action == "importstatus":
	import_mailbox.importStatus()
