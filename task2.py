import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r'\d+\.\d+', text)  #find numbers in the text
    for n in numbers:                        #str to float
        yield float(n)

def sum_profit(text: str, func: Callable):
    return sum(func(text))
