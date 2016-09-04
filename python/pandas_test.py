#!/usr/bin/python env
import random

import pandas as p
import numpy as n

# Generate random list
randlist = [random.randint(1, 50) for _ in range(5)]
print('{0} is type {1}'.format(randlist, type(randlist)))

# Series generation
series = p.Series(randlist)
print('{0} is type {1}'.format(series, type(series)))

# DataRange creation
dates = p.date_range('20161002', periods=len(randlist))
print('{0} is type {1}'.format(dates, type(dates)))

# DataFrame creation
df = p.DataFrame(n.random.randn(len(randlist),4), index=dates, columns=list('ASDF'))
print('{0} is type {1}'.format(df, type(df)))


datalist = ['jim', 'jose', 'jace', 'jack', 'jackson']
datadict = {'A': 19.22,
            'S': p.Categorical(datalist),
            'D': p.Timestamp('20111111'),
            'F': p.Series(randlist, dtype='int32')}

df2 = p.DataFrame(datadict)
print('{0} is type {1}'.format(df2, type(df2)))
