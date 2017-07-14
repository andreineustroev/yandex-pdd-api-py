domain = "domail.org"
api_key = "tokentokentokentokentokentokentoken"

translate = {
	'domain'       : 'Домен',
	'server'       : 'Сервер',
	'success'      : 'Выполнено',
	'error'        : 'Ошибка',
	'login'        : 'Email ящика',
	'uid'          : 'Идентификатор',
	'fio'          : 'ФИО',
	'aliases'      : 'Алиасы',
	'fname'        : 'Фамилия',
	'iname'        : 'Имя',
	'birth_date'   : 'Дата рождения',
	'sex'          : 'Пол',
	'hintq'        : 'Секретный вопрос',
	'ready'        : 'Готовность к использованию',
	'maillist'     : 'Является рассылкой',
	'enabled'      : 'Активен',
	'page'         : 'Страница',
	'pages'        : 'Всего страниц',
	'on_page'      : 'На странице',
	'total'        : 'Всего акаунтов',
	'accounts'     : 'Акаунты'
}

visible_filelds = [
#Possible value
#'fio', 'login', 'enabled', 'birth_date', 'uid', 'sex', 'ready', 'hintq', 'fname', 'iname', 
'fio', 'login', 'enabled', 'birth_date', 'uid', 'sex', 'ready'
]

#imap, imap4, pop, pop3
mailMethod = 'imap'
mailServer = 'mail.artsofte.ru' 
mailPort = 143
#Use ssl yes/no
mailSsl = 'no'