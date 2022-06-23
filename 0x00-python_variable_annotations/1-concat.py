#!/usr/bin/env python3
'''
Task 1 module
Basic annotations - concat
>>> type(concat('',''))
<class 'str'>
'''


def concat(str1: str, str2: str) -> str:
    '''Concatinates two strings provided as arguments'''
    return f'{str1}{str2}'
