#!/usr/bin/env python3
'''python caching'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    defines a basic caching class
    
    Arguments:
        BaseCaching class which defines a parent cache class
    '''

    def put(self, key, item):
        '''
        add cache_data to cache
        Args:
            key(_type): cache_data key
            item(_type):corresponding_data item to the key
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''
        get value linked to the key
        Args:
            key(_type): cache_data key

        Returns:
            _type: None if unsuccessful else data at key
        '''
        return self.cache_data.get(key)