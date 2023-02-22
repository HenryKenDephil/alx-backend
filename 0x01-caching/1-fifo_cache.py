#!/usr/bin/env python3
#FIFO  caching
from functools import cache

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    '''
        defining classs for FIFO caching

        Args:
            BaseCaching (class): parent class
    '''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''
             a function to add  data to the cache
             Args:
                key(_type): key
                item(_type): value
        '''

        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) >  self.MAX_ITEMS:
            key_list = list(self.cache_data.keys())
            del self.cache_data[key_list[0]]
            print(f'DISCARD: {key_list[0]}')

        def get(self, key):
            '''
                get value linked to a specific key
                Args:
                    key(_type): cache_data key

                Returns: 
                    _type: None if  unsuccessful else data at key
            '''

            return self.cache_data.get(key)