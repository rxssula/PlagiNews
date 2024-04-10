# PlagiNews

## Открыть Проект

Чтобы открыть этот проект, сначала вам нужно установить все из requirements.txt:

```
pip install -r requirements.txt
```

либо

```
pip3 install -r requirements.txt
```
Далее вам нужно запустить сервер:

```
python manage.py runserver
```

либо

```
python3 manage.py runserver
```

После этого вам нужно запустить команду для обновления базы данных каждую минуту:

```
python manage.py update_database
```

## Процесс Проектирования и Разработки

На протяжении всего проекта я использовал метод веб-скрейпинга с помощью фреймворка django.

Первая проблема с этим проектом заключалась в том, что я не мог найти подходящего api для казахских новостей. После этого я решил использовать web-scraping.

Для хранения собранных данных я использовал базу данных django. Для хранения собранных данных я использовал базу данных django.  В этой базе данных у меня есть такие атрибуты, как категория, дата, название, ссылка на новость на сайте тенгри и ссылка на изображение.

Для удобства проектирования я использовал шаблонную методологию и bootstrap, чтобы сделать дизайн максимально минималистичным и красивым.

Чтобы сайт показывал новейшие новости был добавлен таймер, который каждую минуту проверяет вышли ли новые новости и соответственно добавляет их в базу данных.

## Ошибки и Проблемы

При попытке добавить дату новости, я столкнулся с проблемой неправильного формата. В связи с чем, решил фильтровать их по дате добавления в базу данных вместо даты добавления в сайт тенгри.

Изначально сайт был полностью основан на веб-скрапинге без базы данных, однако это очень сильно замедляло производительность сайта. Из-за чего была добавлена база данных, чтобы ускорить сайт.

Также при попытке захостить сайт, я столкнулся с многими проблемами, которые я не смог решить и решил избежать хостинг. 

При нажатии на новость, пользователь направляется на статью на сайт tengrinews.kz, вместо сайта проекта. Это было сделано в связи с нагрузкой вне проекта. Также был задан вопрос, обязательно ли презентовать статью на сайте, на что был получен ответ, что не обязательно. 

Поиск осуществляется через веб-скрапинг, так как через базу данных поиск будет выводить новости только по названию либо короткому описанию, однако через веб-скрапинг поиск осуществляется через ключевые слова в самих новостях.


