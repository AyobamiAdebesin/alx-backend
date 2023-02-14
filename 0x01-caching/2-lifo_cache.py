#!/usr/bin/env python3
""" LIFOCache that inherits frm BaseCaching """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Implements a LIFOCache """
    def __init__(self):
        """ Initializes """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ Store data into the cache """
        cache_len = len(self.cache_data)
        if key is None or item is None:
            return None
        if cache_len >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            temp = list(self.cache_data.keys())[0]
            del self.cache_data[temp]
            print("DISCARD: {}".format(temp))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an object from the cache """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
