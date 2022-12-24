# выбрать с сайта json-placeholder данные и записать их в одну папку в разные excel файлы


# import _1first
from _1first import first
from _2second import second
from _3third import third


# json_data = _1first.first()
json_data_raw = first(is_logging=False)           # TODO получение "сырых данных"
json_data_final = second(raw_data=json_data_raw)  # TODO подготовка "сырых данных"
third(final_data=json_data_final)                 # TODO запись "подготовленных" данных
