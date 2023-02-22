#!/usr/bin/env python3
'''caching using lru'''

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    '''
    defines the LRU cache class

    Args:
        BaseCaching (obbj): parent class
    '''

    def __init__(self):
        super().__init__()
        self.stacks = []

    def put(self, key, item):
        '''
        adds data to storag using LRU cache
        
        Args:
            key (str): key
            item (str): value associated with key
        '''

        if not key or  not item:
            return
        
        updated = True if key in self.cache_data.keys() else False

        self.cache_data[key] = item
        self.stacks.append(key)

        if updated:
            self.updated_key = key
            first_index_of_key = self.stacks.index(key)
            del self.stacks[first_index_of_key]
            return
        if len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[self.stacks[0]]
            print(f'DISCARD:{self.stacks[0]}')
            del self.stacks[0]

    def get(self, key):
        '''
        get the value of item at specific key

        Args:
            key (str): key

        Returns:
            str: value if successful else None
        '''

        if key not in self.cache_data.keys():
            return
        
        self.stacks.append(key)
        first_index_of_key = self.stacks.index(key)
        del self.stacks[first_index_of_key]

        return self.cache_data.get(key)