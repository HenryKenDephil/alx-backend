#!/usr/bin/env python3
'''
    simple helper function
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
        a simple helper function that takes two arguments

        arguments:
            page: the page number
            page_size: the number of pages to return

        Returns: the function should return a tuple of size two
            tuple contains a start index and end index
            corresponding to the range of index of indexes to return in a list
    '''
    #start_index = page
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)