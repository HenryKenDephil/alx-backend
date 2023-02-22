#!/usr/bin/env python3
'''LIFO caching'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    define LIFO caching class

    Args:
        BaseCaching (_type): parent cache class
    '''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''
        stores cahced data using LIFO policies

        Args:
            key (str): key
            item (str): value of itme to be stored
        '''

        if not key or not item:
            return
        if key in self.cache_data.keys():
            updated = True

        else:
            updated = False

        self.cache_data[key] = item

        if updated:
            self.updated_key = key
            return
        
        key_list = list(self.cache_data.keys())

        if len(self.cache_data) > self.MAX_ITEMS:
            try:
                del self.cache_data[self.updated_key]
                print(f'DISCARD: {self.updated_key}')
            except Exception:
                del self.cache_data[key_list[-2]]
                print(f'DISCARD: {key_list[-2]}')

        def get(self, key):
            '''
            get value associated with key

            Args:
                key (_type): cache_data key

            Returns:
                _type_: None if unsuccessful else data at key
            '''
            return self.cache_data.get(key)