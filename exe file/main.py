# https://pypi.org/project/python-random-strings/
# https://coding-kindergarten.tistory.com/84

from python_random_strings import random_strings
import time 

for i in range (10):
    a = random_strings.random_lowercase(6)
    print(a)

    time.sleep(1.5)