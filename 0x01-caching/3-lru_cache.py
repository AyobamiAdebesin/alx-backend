#!/usr/bin/env python3
""" Least Recently Used (LRU) Caching """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Least Recently Used Caching

    get(self, key):  takes a key argument and
    returns the corresponding value if it is
    present in the cache. If the key is found,
    the item is moved to the FRONT of the ordered
    dictionary to indicate that it has been recently used

    put(self, key, value): takes a key and value. If
    the key is not present and the cache is not full,
    add the key-value pair to the dict and move it to
    the FRONT of the dict to indicate that it has been recently
    used.
    If key is not present and cache is full, pop the last element
    i.e the element at the BACK out of the dict and set the new
    key value pair and move it to the FRONT of the dict.
    """
    def __init__(self):
        """ Initializes """
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        # If key is not present and max capacity is not full
        # set the key-value pair and move to the right.
        # If key is not present and max capacity is full
        # remove the rightmost value in the dict, set the key-value
        # pair and move to the front of the dict
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                temp, _ = self.cache_data.popitem(True)
                print("DISCARD:", temp)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key."""
        # If key is present, move it to the front(extreme left hand side)
        #  of the dict and return the value
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
