#!/usr/bin/env python3
""" Most Recently Used Caching """
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Defines a Most Recently Used Algorithm """
    def __init__(self):
        """ Initializes """
        super.__init__(self)
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Store data into the cache """
        if key is None and item is None:
            return None
        cache_len = len(self.cache_data)
        if key not in self.cache_data and cache_len >= BaseCaching.MAX_ITEMS:
            temp, _ = self.cache_data.popitem(key)
            print("DISCARD: {}".format(temp))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Get data from the cache """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data[key]
