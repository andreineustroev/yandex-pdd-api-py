#!/bin/bash

echo "!!! Запрос пользователей ./api.py get all"
./api.py get all

echo "!!! Добавление пользователя test ./api.py create test 123QWE123"
./api.py create test 123QWE123

echo "!!! Запрос пользователей ./api.py get all"
./api.py get all

echo "!!! Изменения пароля test ./api.py modifypass 123456qwerty"
./api.py modifypass test 123456qwerty

echo "!!! Изменения имени test ./api.py modifyname Тест Тестович"
./api.py modifyname test Тест Тестович

echo "!!! Изменения пола test ./api.py modifysex 1"
./api.py modifysex test 1

echo "!!! Дективация test ./api.py modifyen no"
./api.py modifyen test no

echo "!!! Удаление пользователя test ./api.py delete test"
./api.py delete test
