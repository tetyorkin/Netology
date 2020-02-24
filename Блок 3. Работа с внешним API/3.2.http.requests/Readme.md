![GitHub last commit](https://img.shields.io/github/last-commit/tetyorkin/Netology?style=plastic)
# Домашнее задание к лекции 3.2 «Работа с библиотекой requests, http-запросы»

Исходный код для выполнения домашней работы вы найдете в папке [3.2.http.requests](https://github.com/netology-code/py-homework-basic-files/tree/master/3.2.http.requests).

## Задача №1
Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:

* Путь к файлу с текстом;
* Путь к файлу с результатом;
* Язык с которого перевести;
* Язык на который перевести (по-умолчанию русский).

У вас есть 3 файла (`DE.txt`, `ES.txt`, `FR.txt`) с новостями на 3 языках: французском, испанском, немецком. Функция должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.

Для переводов можно пользоваться [API Yandex.Переводчик](https://tech.yandex.ru/translate/).

## \*Задача №2
Научиться работать с api [Яндекс.Диска](https://yandex.ru/dev/disk/rest/)
Написать программу, которая загружает переведенные файлы на Яндекс.Диск. 
[Документация по загрузке файлов](https://yandex.ru/dev/disk/api/reference/upload-docpage/)
Токен можно получить на [Полигоне](https://yandex.ru/dev/disk/poligon/) кликнув по кнопке "Получить OAuth-токен"

## Результат выполнения задачи №2
В консоли

![Image alt](https://raw.githubusercontent.com/tetyorkin/Netology/master/%D0%91%D0%BB%D0%BE%D0%BA%203.%20%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%81%20%D0%B2%D0%BD%D0%B5%D1%88%D0%BD%D0%B8%D0%BC%20API/img/result_pycharm.png)

 на диске
![Image alt](https://raw.githubusercontent.com/tetyorkin/Netology/master/%D0%91%D0%BB%D0%BE%D0%BA%203.%20%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%81%20%D0%B2%D0%BD%D0%B5%D1%88%D0%BD%D0%B8%D0%BC%20API/img/result_disk_1.png)

![Image alt](https://raw.githubusercontent.com/tetyorkin/Netology/master/%D0%91%D0%BB%D0%BE%D0%BA%203.%20%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%20%D1%81%20%D0%B2%D0%BD%D0%B5%D1%88%D0%BD%D0%B8%D0%BC%20API/img/result_disk_2.png)