# 1. možnost
import data
print(data.my_data)

# 2. možnost
from data import my_data
print(my_data)

# 3. možnost
from data import *

# 4. možnost - metoda alias
import data as d
print(d.my_data)