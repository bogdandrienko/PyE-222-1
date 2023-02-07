# cmd
# python -m venv env              # python3 -m venv env
# call env/Scripts/activate.bat   # source env/bin/activate
# pip install requests
# pip freeze > requirements.txt
# pip install -r requirements.txt
import time

# https://tproger.ru/articles/computational-complexity-explained/
# https://habr.com/ru/post/188010/

t_start = time.perf_counter()

for i in range(1, 1000):  # N
    for j in range(1, 1000):  # N
        print(i, j)

# O(N) - на грани
# 0.0003  - 100
# 0.07    - 100
# 7.0     - 1000
# 0.003   - 1000

# 0.03    - 10000

# 10000 * 1 = получить, обработать(от легко до очень тяжело), сохранить в базу (тяжело)
# 1000 * 1 * 60 * 60 * 3 = 10 800 000

t_stop = time.perf_counter()
print("Заняло времени: ", round(t_stop-t_start, 5), " секунд")


# O(n) — линейная сложность 1000s * 1e = 1000=e/s
# O(n2)
# O(log n) — логарифмическая сложность
# 0(1) -

list1 = [1, 2, 3, 4, 5, 6, 7]
elem = 6
for i in list1:  # O(n)
    if i == elem:
        print("Нашёл")

