import for_import
from for_import import difference, Store
# from for_import import *  # ! TODO BAD = collisions
import for_import as for_i  # alias

print(for_import.summing(12, 13))
print(for_i.summing(12, 13))
print(difference(12, 13))
print(for_i.sum(12, 13))

print(Store.Calculator.difference(1, 2))
print(Store.DateTimes.get_current_time())
