#!/usr/bin/env python3
""" FIFOCache that inherits from BaseCaching """

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Caching system """
    def __init__(self):
        """ Initializes """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ Store data inside the cache """
        cache_len = len(self.cache_data)
        if key is None or item is None:
            pass
        if cache_len >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            temp = list(self.cache_data.keys())[0]
            del self.cache_data[temp]
            print("DISCARD: {}".format(temp))
        self.cache_data[key] = item

    def get(self, key):
        """ Get data from the cache """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
