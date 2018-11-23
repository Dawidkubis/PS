"""
This is a great file with some of the stuff I will be using consistently
            - DAWID J. KUBIS
"""
#from abc import *
from time import time
import functools

#---------decorators-------#
def timer(func):
    """
    Use as a decorator
    Prints the time it takes a function to run
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        output = func(*args, **kwargs)
        end = time()
        print(f'Finished {func.__name__} in {end - start} secs')
        return output
    return wrapper


#---------decorators-------#
#---------functions--------#
def generate_primes(lim):
    """
    Generates primes up to a certain limit,
    limit is not included
    """
    primes = []
    nums = list(range(2, lim))
    while nums != []:
        primes.append(nums[0])
        nums = [i for i in nums if i%primes[-1] != 0]
    return primes
#---------functions--------#
#---------classes----------#
class MError(Exception):
    """
    An Exception with a message
    Should be printed after catching
    """

    def __init__(self, msg):
        super().__init__()
        self.msg = msg
        print('----------ERROR---------')

#---------classes----------#
if __name__ in ('__main__', '__console__'):
    print('''
          THIS IS A MODULE
          
          Meaning it Should not be run as __main__ or __console__

          dumbass
          ''')
