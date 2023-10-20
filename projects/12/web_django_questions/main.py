"""
Так что же такое Джанго?

Python веб-фреймворк.

#########################
Каковы наиболее важные особенности Django?

- больше наработок
- Универсальность
- большое количество встроенных библиотек
- лёгкие написание
- хорошая защита
- экосистема Python

#########################
Что такое CRUD?

- Create Read Update Delete
- базовые операции с базой данных

#############################

Есть ли у Django недостатки?

- монолит (+легче разворачивать, на первых быстрее разработка.)
- Все зависит от ORM (sql на Python)

###############################
Как выглядит архитектура Django?

- MVT(C) -
- Model - база данных (сырая)
- View - бизнес логика (def vs class)
- Template - отображение (внешний вид)

###############################
Explain the Django project directory structure.

- web (весь проект)
-   - django_app1 (приложение)
-   - django_app2 (приложение)
-   - django_settings (настройки проекта)

###############################
What are models in Django?
- представление базы данных
- каждая модель это таблица
- параметры модели - столбцы и настройки таблицы

#############################
What is Jinja templating?
- шаблонизатор
- позволяет внутри html писать python-like код

- не подходит для django DRF
- JS фреймворки(Angular, Vue, React...) - интерактивнее, красочнее, быстрее

#############################

Discuss Django’s Request/Response Cycle.
User(url) -> cdn(hosting) -> ip -> ubuntu -> nginx -> gunicorn -> django(x10) ->
postgres(api/db/file) -> django -> gunicorn -> nginx -> ubuntu -> cdn(hosting) -> User(frontend)

#############################

What is the Django Admin interface?

- встроенная библиотека и дополнение к django, где суперпользователи/модераторы
могут просматривать данные из базы данные в удобном визуальном формате (CRUD)

#############################

What are signals in Django?

- с моделями можно выполнять действия (CRUD)
- иногда нужно при создании пользователя, создавать ему автоматический
профиль.(dispatch-receiver)

##############################

What are the different model inheritance styles in Django?
- Какие "стили" наследования есть в Django для моделей

- Нам не хватает стандартной модели пользователя.
- 1) Выполнить наследование от родителя и переопределить.(
- При изменении стандартной модели могут пострадать все взаимосвязаннные
функции. JWT-tokens
)

- 2) Multi-table inheritance (
- Создали ещё одну таблицу, и просто "привязали" её к стандартной.
)



#############################
What databases are supported by Django?

PostgreSQL
MySQL
Oracle
SQLite

#############################
What are Django.shortcuts.render functions?

- рендерит html - возвращает указанную html страницу
- HttpResponse
- JsonResponse(Response - DRF)

#################################

What is the Django Rest Framework?

- библиотека-дополнение для Django
- помогает создавать API (Rest, Rest-Api, Restfull)

#################################

What do you use middleware for in Django?

- промежуточный слой для приложений и всех запросов
- выполняет какие-то действия на request/response

- декораторы, которые можно по желанию накладывать
на выбранные функции, немного гибче.

#################################

How can you see raw SQL queries running in Django?

from Django.db import connection

#################################

List several caching strategies supported by Django.

- В оперативе(Locmem - прям на Django, Redis - linux)
- В базе данных
- В файле


#################################

What is mixin?

class NeedAuth - требует авторизацию
class Salt - солёная и быстрее закипает

class ListObject - возвращает массив объектов

class ViewGetNews(ListObject, NeedAuth) - mixin(множественное наследование)

#################################

"""
