import numpy as np

a = np.arange(10)

# default is 64 bit integer
print(a.dtype)

x = 2*a

# also has widespread use in digital audio
# unsigned 16 bit integer
b = np.arange(7, dtype=np.uint16)