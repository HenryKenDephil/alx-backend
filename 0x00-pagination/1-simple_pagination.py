#!/usr/bin/env python3
#implement method get_page

import csv
import math
from typing import List, Tuple 

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
class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        the method takes tow integer arguments page and page_size
        the default value is 10
        the CSV file must be used
        the implementation must use assert to verify that arguments
        are integers and greater than 0
        uses index_range to find correct indexes to paginnate dataset
        Returns empty list if input arg is out of range
        '''

        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        self.dataset()

        if self.__dataset is None:
            return []

        idx_range = index_range(page, page_size)
        data = self.__dataset[idx_range[0]:idx_range[1]]
        return data       