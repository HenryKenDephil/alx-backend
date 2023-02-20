#!/usr/bin/env python3
#hypermedia paginations

import csv
import math
from typing import List, Tuple
from math import ceil

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
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns all necessary key value pairs for pagination
        Args:
            page (int, optional): page index. Defaults to 1.
            page_size (int, optional): number of items in page. Defaults to 10.
        Returns:
            dict: dictionary of pagination attributes
        """
        data = self.get_page(page, page_size)
        dataset_length = len(self.dataset())

        try:
            total_pages = ceil(dataset_length / page_size)
        except Exception:
            total_pages = 0

        next_page = page + 1 if page < total_pages else None

        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }