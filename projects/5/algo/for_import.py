import datetime
import time


def summing(a: int | float, b: int | float) -> int | float:
    return a + b


def difference(a: int | float, b: int | float) -> int | float:
    return a - b


def sum(a: int | float, b: int | float) -> int | float:
    return a / b


class Store:
    class Calculator:
        @staticmethod
        def summing(a: int | float, b: int | float) -> int | float:
            return a + b

        @staticmethod
        def difference(a: int | float, b: int | float) -> int | float:
            return a - b

        @staticmethod
        def sum(a: int | float, b: int | float) -> int | float:
            return a / b

    class DateTimes:
        @staticmethod
        def get_current_datetime(timezone=6):
            return datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        @staticmethod
        def get_current_time(timezone=6):
            return datetime.datetime.now().strftime("%H:%M:%S")

        @staticmethod
        def example_time_measure() -> None:
            t_start = time.perf_counter()
            #
            time.sleep(1.0)  # тут должны быть интенстивные алгоритмы
            #
            t_stop = time.perf_counter()
            print(round(t_stop - t_start, 7))
