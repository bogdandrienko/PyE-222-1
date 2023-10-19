from django.db import models

# Create your models here.

# Author
# id
# first_name
# last_name
# ...

# Category
# id
# name
# rating
# ...

# Book
# id
# name
# author ForeignKey(Author)
# category
# ...

"""
SELECT id, name, author(id), category(id) FROM Book

SELECT 
b1.id AS id, 
b1.name AS name, 
a1.last_name || " " || a1.first_name AS author, 
c1.rating 
FROM Book AS b1
INNER JOIN Category AS c1 ON b1.category = c1.id
INNER JOIN Author AS a1 ON b1.author = a1.id
"""

# only/defer
"""
Book.objects.all()  # SELECT *
.only('title', 'author') - выбирать только указанные поля
.defer('description', 'publication_date') - не выбирать указанные поля
- экономия, оптимизация

"""

# select_related - аналог JOIN-а в ORM
"""
Book.objects.all().select_related("author")  # ForeignKey(O2M, O2O)
# .select_related("city", "city__country") # принудительно
- 1 Война и мир Лев Толстой
"""

# prefetch_related - аналог JOIN-а в ORM
"""
Book.objects.all().prefetch_related("author")  # ManyToMany
- 1 Война и мир Лев Толстой
- 1 Война и мир Лермонтов

"""

"""
Категория

Автор

Книга
id
ca(O2O) - А
ca(O2M) - А
au(M2M) - А, Б, С
"""

