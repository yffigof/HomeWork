from django.http import HttpResponse

def index(request):
    return HttpResponse('Домашка по 4 занятию: '
                        '   1.  '
                        'Выберите верные утверждения касательно клиент-серверного взаимодействия: '
                        'Клиент-серверная архитектура — такая архитектура, в рамках которой есть сервер, у которого есть необходимые данные (какая-либо информация), и клиент, которые эти данные хочет получить. '
                        'Сервер инициирует обращение к клиенту и тот отдает ему необходимую информацию. Другими словами, сервер делает запрос, а клиент возвращает ответ. '
                        'Данная реализация взаимодействия клиента-сервера строится на специальном протоколе, который называется HyperText Transfer Protocol (HTTP) или протокол передачи гипертекста. '
                        'Сообщения клиента называют запросами, а сообщения сервера — ответами. '
                        ''
                        '           2.          '
                        'Сопоставьте HTTP-запросы и их назначение '
                        'А) GET            |             1) Запрос на добавление данных '
                        'Б) POST           |             2) Запрос на получение данных '
                        'В) DELETE         |             3) Запрос на обновление данных '
                        'Г) PUT            |             4) Запрос на удаление данных '
                        ''
                        '       3.     ' 
                        'Перетяните в нужные ячейки подходящие по смыслу слова '
                        'MVT   MVC   MODEL   View   Template   База данных   Сервер   Django '
                        'Вставьте пропущенные слова в текст'
                        'Django использует     — архитектуру, которая является частным случаем    архитектуры. Логика работы веб-приложения в '
                        'Django разделена на некоторые уровни. Уровень   описывает работу с базой данных. Уровень   описывает основную '
                        'логику нашей программы. То, как мы обрабатываем полученные данные, какие данные хотим отобразить, куда и что сохраняем и т. д. Это '
                        'уровень, с которым непосредственно взаимодействует пользователь, когда отправляет запрос. Уровень   описывает то, как '
                        'информация будет отображаться для пользователя.'
                        '                                              '
                        '            4.           ' 
                        'В рамках проекта с вебинара создайте еще одно приложение таким же образом, как мы делали на занятии и дайте ему название '
                        'app_lesson_4. Создайте в нем представление (view), которое будет возвращать ответ: «Домашка по 4 занятию». Подключите приложение к '
                        'проекту. Сделайте, так, чтобы представление работало по следующему адресу: http://127.0.0.1/lesson_4. '
                        'В качестве решения прикрепите ссылку на репозиторий git.')