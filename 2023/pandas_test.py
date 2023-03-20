from pandas import Series, DataFrame

import pandas as pd

obj = Series([4, 5, 6, -7])
print(obj)
print(obj.index)
print(obj.values)


data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])

print(frame)
print(frame2)
