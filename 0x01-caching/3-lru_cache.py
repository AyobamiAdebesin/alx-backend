#!/usr/bin/env python3
""" Least Recently Used (LRU) Caching """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Least Recently Used Caching """
    def __init__(self):
        """ Initializes """
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Store data into the cache """
        cache_len = len(self.cache_data)
        if key is not None and item is not None:
            if cache_len < BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                else:
                    self.cache_data[key] = item
                    self.cache_data.move_to_end(key, last=False)
            elif cache_len >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                else:
                    temp = self.cache_data.popitem(last=False)
                    print("DISCARD: {}".format(temp))
                    self.cache_data[key] = item
                    self.cache_data.move_to_end(key)
        else:
            pass

    def get(self, key):
        """ Get items from the cache """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data
        else:
            return None
