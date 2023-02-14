#!/usr/bin/env python3
""" A BasicCache class that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Inherits from BasicCaching """
    def __init__(self):
        """ Initializes"""
        pass

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get the items from the cache with a key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return (self.cache_data.get(key))
